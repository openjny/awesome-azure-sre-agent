# 用途: 指定ドメインの SSL/TLS 証明書の有効期限・発行者・リスクレベルを返す
# 引数:
#   domain (str, required): チェック対象のドメイン (例: api.contoso.com)
#   port   (str, optional): 接続ポート (デフォルト: 443)
# 前提パッケージ: 標準ライブラリのみ (ssl, socket, datetime)
# 出典: https://techcommunity.microsoft.com/blog/appsonazureblog/build-a-custom-ssl-certificate-monitor-with-azure-sre-agent-from-python-tool-to-/4495832

import ssl
import socket
from datetime import datetime, timezone


def main(domain, port="443"):
    """Check SSL certificate expiry for a domain."""
    port = int(port)
    context = ssl.create_default_context()

    try:
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        not_before = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
        not_after = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        days_remaining = (not_after - now).days

        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject = dict(x[0] for x in cert.get("subject", []))

        if days_remaining < 0:
            risk_level = "EXPIRED"
        elif days_remaining <= 7:
            risk_level = "CRITICAL"
        elif days_remaining <= 30:
            risk_level = "WARNING"
        elif days_remaining <= 60:
            risk_level = "ATTENTION"
        else:
            risk_level = "HEALTHY"

        san_list = []
        for entry_type, value in cert.get("subjectAltName", []):
            if entry_type == "DNS":
                san_list.append(value)

        return {
            "domain": domain,
            "port": port,
            "status": "valid" if days_remaining >= 0 else "expired",
            "risk_level": risk_level,
            "days_remaining": days_remaining,
            "not_before": not_before.isoformat(),
            "not_after": not_after.isoformat(),
            "issuer": issuer.get("organizationName", "Unknown"),
            "issuer_cn": issuer.get("commonName", "Unknown"),
            "subject_cn": subject.get("commonName", domain),
            "serial_number": cert.get("serialNumber", "Unknown"),
            "version": cert.get("version", "Unknown"),
            "san_count": len(san_list),
            "san_domains": san_list[:10],
            "checked_at": now.isoformat(),
        }

    except ssl.SSLCertVerificationError as e:
        return {
            "domain": domain,
            "port": port,
            "status": "verification_failed",
            "risk_level": "CRITICAL",
            "error": str(e),
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }
    except (socket.timeout, socket.gaierror, ConnectionRefusedError, OSError) as e:
        return {
            "domain": domain,
            "port": port,
            "status": "connection_failed",
            "risk_level": "UNKNOWN",
            "error": str(e),
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }
