# -*- coding: utf-8 -*-
"""Dropship Split-Shipment Optimizer for GenPark Agentic Commerce."""
import json
from typing import Dict, Any, List

class DropshipSplitShipmentOptimizer:
    @staticmethod
    def optimize_order_routing_matrix(sku_quantities: Dict[str, int], warehouse_availability: Dict[str, Dict[str, int]], shipping_rates_by_origin: Dict[str, float]) -> Dict[str, Any]:
        # Check if single warehouse has all SKUs
        single_wh_candidates = []
        for wh, inv in warehouse_availability.items():
            if all(inv.get(sku, 0) >= qty for sku, qty in sku_quantities.items()):
                single_wh_candidates.append((wh, shipping_rates_by_origin.get(wh, 15.0)))
        
        if single_wh_candidates:
            best_wh, best_cost = min(single_wh_candidates, key=lambda x: x[1])
            return {
                "routing_strategy": "CONSOLIDATED_SINGLE_SHIPMENT",
                "assigned_warehouse": best_wh,
                "split_count": 1,
                "total_shipping_cost_usd": best_cost,
                "customer_delivery_experience": "OPTIMAL_SINGLE_PACKAGE"
            }
        
        # Split necessary
        assigned = {}
        total_cost = 0.0
        for sku, qty in sku_quantities.items():
            wh_found = "DEFAULT_3PL"
            for wh, inv in warehouse_availability.items():
                if inv.get(sku, 0) >= qty:
                    wh_found = wh
                    break
            assigned[sku] = wh_found
        
        distinct_whs = list(set(assigned.values()))
        for wh in distinct_whs:
            total_cost += shipping_rates_by_origin.get(wh, 12.0)
            
        return {
            "routing_strategy": "SPLIT_MULTI_ORIGIN_SHIPMENT",
            "assigned_warehouses": distinct_whs,
            "split_count": len(distinct_whs),
            "sku_origin_map": assigned,
            "total_shipping_cost_usd": round(total_cost, 2),
            "customer_delivery_experience": "MULTI_PACKAGE_TRACKING"
        }

    @staticmethod
    def calculate_split_shipment_economic_penalty(single_box_rate_usd: float, multi_box_rates_usd: List[float], extra_packaging_cost_usd: float = 1.75) -> Dict[str, Any]:
        split_total_shipping = sum(multi_box_rates_usd)
        extra_boxes = max(0, len(multi_box_rates_usd) - 1)
        total_split_cost = split_total_shipping + (extra_boxes * extra_packaging_cost_usd)
        margin_drag = round(total_split_cost - single_box_rate_usd, 2)
        
        return {
            "baseline_single_box_usd": single_box_rate_usd,
            "split_packages_count": len(multi_box_rates_usd),
            "total_split_fulfillment_cost_usd": round(total_split_cost, 2),
            "split_shipping_margin_drag_usd": margin_drag,
            "profitability_verdict": "MARGIN_EROSIVE" if margin_drag > 8.0 else "ACCEPTABLE_OVERHEAD"
        }
