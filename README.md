# Awesome Azure SRE Agent

> 🌐 [日本語版はこちら (Japanese)](README.ja.md)

This repository collects official documentation, use case scenarios, demo videos, case studies, and resource definitions for Azure SRE Agent. Use it as a reference when adopting and utilizing Azure SRE Agent.

**Table of Contents**

- [🔗 Official Links](#-official-links)
- [🚀 Use Case Scenarios](#-use-case-scenarios)
- [🔌 MCP Integration Guide](#-mcp-integration-guide)
- [🎬 Demo Videos](#-demo-videos)
- [🖥️ Demo Applications](#-demo-applications)
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

## 🎬 Demo Videos

- **[Use Azure SRE Agent to automate tasks and increase site reliability (Microsoft Build 2025 / DEM550)](https://build.microsoft.com/en-US/sessions/DEM550)**  
  Demo session from Microsoft Build 2025. Shows how SRE Agent executes a series of tasks just by describing intent in natural language, using an e-commerce site incident response scenario
- **[Proactive .NET Reliability with Azure SRE Agent](https://www.youtube.com/watch?v=Kx_6SB-mhgg)**  
  Using an ASP.NET app, demonstrates proactive reliability improvement by detecting and fixing issues before incident reports come in

## 🖥️ Demo Applications / Environments

- **[azure-sre-agent-demokit (ussvgr/GitHub)](https://github.com/ussvgr/azure-sre-agent-demokit)**  
  A kit for bulk provisioning Azure SRE Agent demo environments with Terraform. Creates a .NET Blazor demo app, Application Insights alerts, and SRE Agent resources together

## 📣 Case Studies

- **[Future of Incident Response with Azure SRE Agent x PagerDuty (AEON Smart Technology / AEON TECH HUB #23)](https://speakerdeck.com/aeonpeople/the-future-of-incident-response-azure-sre-agent-x-pagerduty)**  
  Practical report on integrating PagerDuty with Azure SRE Agent to automate from incident detection through autonomous investigation to recovery

## 📚 Other Resources

- **[Context Engineering Lessons from Building Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200/)**  
  Lessons in context engineering from the SRE Agent development team covering tool design, multi-agent, code execution, and compaction
- **[Reactive Incident Response with Azure SRE Agent: From Alert to Resolution in Minutes](https://techcommunity.microsoft.com/blog/azurearchitectureblog/reactive-incident-response-with-azure-sre-agent-from-alert-to-resolution-in-minu/4492938)**  
  Full flow demo from alert firing to autonomous investigation, approval-based remediation, and recovery verification for 2 scenarios: SQL connection failure and VM CPU spike. Also covers custom IRP procedure writing and setup

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
