# Awesome Azure SRE Agent

> 🌐 [日本語版はこちら (Japanese)](README.ja.md)

This repository collects official documentation, use case scenarios, demo videos, case studies, and resource definitions for Azure SRE Agent. Use it as a reference when adopting and utilizing Azure SRE Agent.

**Table of Contents**

- [🔗 Official Links](#-official-links)
- [🚀 Use Case Scenarios](#-use-case-scenarios)
- [🔌 MCP Integration Guide](#-mcp-integration-guide)
- [🎬 Demo Videos](#-demo-videos)
- [🧪 Lab Environments](#-lab-environments)
- [📣 Case Studies](#-case-studies)
- [📚 Other Resources](#-other-resources)
- [🛠️ Resource Definitions](#-resource-definitions)

## 🔗 Official Links

- ⭐ **[Azure SRE Agent Overview](https://learn.microsoft.com/azure/sre-agent/overview)**  
  Official documentation
- ⭐ **[Azure SRE Agent tag - Microsoft Tech Community](https://techcommunity.microsoft.com/tag/azure%20sre%20agent)**  
  Official blog posts and community contributions
- ⭐ **[microsoft/sre-agent](https://github.com/microsoft/sre-agent)**  
  Bug reports, feedback, and Subagent sample collection
- **[Azure SRE Agent Portal Documentation](https://sre.azure.com/docs/overview)**  
  Operation guide on the portal
- **[Azure MCP Center - Microsoft](https://mcp.azure.com/?vendors.microsoft=true)**  
  MCP servers provided by Microsoft

## 🚀 Use Case Scenarios

**Scheduled Task**

- **[Azure WAF Compliance with MCP-Driven SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-waf-compliance-with-mcp-driven-sre-agent/4494687)**  
  Periodically evaluates resource compliance and suggests remediation commands based on the 5 pillars of Well-Architected Framework (WAF) and organization-specific best practices
- **[Build a Custom SSL Certificate Monitor with Azure SRE Agent: From Python Tool to Production Skill](https://techcommunity.microsoft.com/blog/appsonazureblog/build-a-custom-ssl-certificate-monitor-with-azure-sre-agent-from-python-tool-to-/4495832)**  
  Creates a Python tool to monitor SSL certificate expiration and runs periodic health checks

**Incident Response**

- TBD

## 🔌 MCP Integration Guide

- **[How to Connect Azure SRE Agent to Azure MCP](https://techcommunity.microsoft.com/blog/appsonazureblog/how-to-connect-azure-sre-agent-to-azure-mcp/4488905)**  
  Use Azure MCP Server to operate Azure resources in a different way from native az commands
- **[Get started with Dynatrace MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-dynatrace-mcp-server-in-azure-sre-agent/4492363)**  
  Use Dynatrace MCP Server to run Dynatrace capabilities (DQL queries, problem investigation, security vulnerability analysis, time-series forecasting, etc.) from SRE Agent
- **[Get started with Elasticsearch MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-elasticsearch-mcp-server-in-azure-sre-agent/4492896)**  
  Build a Subagent using Elasticsearch's Agent Builder MCP endpoint to perform natural language log search, ES|QL execution, and cluster health checks
- **[MCP-Driven Azure SRE for Databricks](https://techcommunity.microsoft.com/blog/appsonazureblog/mcp-driven-azure-sre-for-databricks/4494630)**  
  Deploy Databricks MCP Server to Azure Container Apps for automated workspace best-practice compliance validation (Scheduled Task) and autonomous root-cause investigation and remediation of job failures (Incident Response)
- **[Get started with Atlassian Rovo MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-atlassian-rovo-mcp-server-in-azure-sre-agent/4497122)**  
  Connect Azure SRE Agent to Jira, Confluence, Compass, and Jira Service Management using the official Atlassian Rovo MCP server
- **[Get started with Datadog MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-datadog-mcp-server-in-azure-sre-agent/4497123)**  
  Use the official Datadog MCP server to interact with logs, metrics, APM traces, monitors, incidents, dashboards, and more from Azure SRE Agent
- **[Get started with PagerDuty MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-pagerduty-mcp-server-in-azure-sre-agent/4497124)**  
  Connect Azure SRE Agent to PagerDuty using the official PagerDuty MCP server for incidents, on-call schedules, services, escalation policies, and more
- **[New in Azure SRE Agent: Log Analytics and Application Insights Connectors](https://techcommunity.microsoft.com/blog/appsonazureblog/new-in-azure-sre-agent-log-analytics-and-application-insights-connectors/4509649)**  
  Native connectors backed by the Azure MCP Server (`monitor` namespace) that let the agent run KQL queries against Log Analytics workspaces and Application Insights resources during investigations, with automatic RBAC setup

## 🎬 Demo Videos

- **[Use Azure SRE Agent to automate tasks and increase site reliability (Microsoft Build 2025 / DEM550)](https://build.microsoft.com/en-US/sessions/DEM550)**  
  Demo session from Microsoft Build 2025. Shows how SRE Agent executes a series of tasks just by describing intent in natural language, using an e-commerce site incident response scenario
- **[Proactive .NET Reliability with Azure SRE Agent](https://www.youtube.com/watch?v=Kx_6SB-mhgg)**  
  Using an ASP.NET app, demonstrates proactive reliability improvement by detecting and fixing issues before incident reports come in

## 🧪 Lab Environments

- **[azure-sre-agent-demokit (ussvgr/GitHub)](https://github.com/ussvgr/azure-sre-agent-demokit)**  
  A kit for bulk provisioning Azure SRE Agent demo environments with Terraform. Creates a .NET Blazor demo app, Application Insights alerts, and SRE Agent resources together
- **[azure-sre-agent-demo (jiratouchmhp/GitHub)](https://github.com/jiratouchmhp/azure-sre-agent-demo)**  
  Hands-on demo environment with a multi-tier app (React + .NET 8 + PostgreSQL), intentional security/cost/availability issues, and scripts to trigger live incidents for customer presentations
- **[azure-sre-agent-sandbox (matthansen0/GitHub)](https://github.com/matthansen0/azure-sre-agent-sandbox)**  
  AKS-based demo lab with 10 breakable scenarios (OOMKilled, CrashLoop, NetworkBlock, etc.), full observability stack, and ready-to-use scripts for deployment and teardown
- **[azure-sre-agent (pelithne/GitHub)](https://github.com/pelithne/azure-sre-agent)**  
  Tools for simulating errors and load testing in AKS clusters. Includes a configurable memory leak Python app and nginx deployment for testing SRE Agent diagnosis

## 📣 Case Studies

- **[Future of Incident Response with Azure SRE Agent x PagerDuty (AEON Smart Technology / AEON TECH HUB #23)](https://speakerdeck.com/aeonpeople/the-future-of-incident-response-azure-sre-agent-x-pagerduty)**  
  Practical report on integrating PagerDuty with Azure SRE Agent to automate from incident detection through autonomous investigation to recovery

## 📚 Other Resources

- **[Context Engineering Lessons from Building Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200/)**  
  Lessons in context engineering from the SRE Agent development team covering tool design, multi-agent, code execution, and compaction
- **[Reactive Incident Response with Azure SRE Agent: From Alert to Resolution in Minutes](https://techcommunity.microsoft.com/blog/azurearchitectureblog/reactive-incident-response-with-azure-sre-agent-from-alert-to-resolution-in-minu/4492938)**  
  Full flow demo from alert firing to autonomous investigation, approval-based remediation, and recovery verification for 2 scenarios: SQL connection failure and VM CPU spike. Also covers custom IRP procedure writing and setup
- **[Azure SRE Agent Architecture and Creation: Practical Benefits for SAP on Azure Customers](https://techcommunity.microsoft.com/blog/microsoftmissioncriticalblog/azure-sre-agent-architecture-and-creation-practical-benefits-for-sap-on-azure-cu/4497625)**  
  Overview of SRE Agent architecture and how it delivers practical benefits for SAP on Azure workloads through automated diagnostics, root cause analysis, and guided remediation
- **[Azure SRE Agent at Microsoft Build 2026: Bringing agentic operations to the enterprise](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-at-microsoft-build-2026-bringing-agentic-operations-to-the-enter/4524669)**  
  Umbrella post for the five Build 2026 releases (VNet integration, Managed Connectors, granular permissions, native GitHub Enterprise support, Private Plugins Marketplace) that focus on enterprise adoption at scale
- **[VNet integration for Azure SRE Agent (preview)](https://techcommunity.microsoft.com/blog/appsonazureblog/vnet-integration-for-azure-sre-agent-preview/4524287)**  
  Route the agent's outbound traffic through a delegated subnet in your own VNet with your NSG rules and private DNS. Covers the three egress modes (Unrestricted / Limited / Azure VNet), the managed-infra bypass path for package registries and code repositories, and configuration guidance
- **[Managed Connectors for SRE Agent (preview) - Govern what your agent can do](https://techcommunity.microsoft.com/blog/appsonazureblog/managed-connectors-for-sre-agent-preview--govern-what-your-agent-can-do/4524840)**  
  Next-generation connector experience with an expanded SaaS catalog (OneDrive, SharePoint, Google Drive, GitLab, Power BI, Microsoft Security Copilot, etc.), per-tool operation selection, pinned parameter values, per-tool Allow/Ask approval, and credential isolation outside the agent's trust boundary
- **[Shaping what Azure SRE Agent does: Tool Permissions and Hooks](https://techcommunity.microsoft.com/blog/appsonazureblog/shaping-what-azure-sre-agent-does-tool-permissions-and-hooks/4524791)**  
  Global tool access policies with allow / ask / deny rules at Global / Agent / Thread scope, plus Command and Prompt Hooks that run before a tool call to block, rewrite, or redirect it based on the actual invocation parameters
- **[Bring Your Own GitHub App: Connecting Azure SRE Agent to Enterprise Repositories](https://techcommunity.microsoft.com/blog/appsonazureblog/bring-your-own-github-app-connecting-azure-sre-agent-to-enterprise-repositories/4524673)**  
  First-class BYO GitHub App authentication for GitHub Enterprise Cloud (`*.ghe.com`) and github.com. The App's private key stays in Azure Key Vault; the agent's managed identity mints short-lived installation tokens at runtime
- **[Private Plugins with Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/private-plugins-with-azure-sre-agent/4523763)**  
  Host plugin marketplaces in private GitHub / GitHub Enterprise repositories to distribute organization-approved skills, runbooks, and MCP tools across every SRE Agent, with OAuth / PAT / GitHub App authentication and version pinning at install time

## 🛠️ Resource Definitions

### Subagent

TBD

### Skill

TBD

### Connector

TBD

### Tools

- **[check_ssl_certificate_expiry.py](resources/tools/python/check_ssl_certificate_expiry.py)**  
  Returns SSL/TLS certificate expiration date, issuer, and risk level for a specified domain
