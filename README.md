# Dropship Multi-Origin Fulfillment & Split-Shipment Cost Minimizer Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Multi-origin fulfillment routing, box consolidation penalty vs split shipping cost minimization, and transit time SLA compliance. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `optimize_order_routing_matrix`: Select cheapest fulfillment combination across multiple origin warehouses taking inventory availability into account.
- `calculate_split_shipment_economic_penalty`: Calculate net operational penalty of splitting cart across multiple packages vs backorder delay.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_dropship_split_shipment_optimizer_skill.server --test
```
