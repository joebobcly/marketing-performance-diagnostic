import pandas as pd

data = pd.read_csv("data/marketing_performance_sample.csv")

previous = data[data["period"] == "Previous"]
current = data[data["period"] == "Current"]

comparison = previous.merge(
    current,
    on="campaign",
    suffixes=("_previous", "_current")
)

comparison["spend_change_pct"] = ((comparison["spend_current"] / comparison["spend_previous"]) - 1) * 100
comparison["pipeline_change_pct"] = ((comparison["pipeline_current"] / comparison["pipeline_previous"]) - 1) * 100
comparison["impressions_change_pct"] = ((comparison["impressions_current"] / comparison["impressions_previous"]) - 1) * 100
comparison["clicks_change_pct"] = ((comparison["clicks_current"] / comparison["clicks_previous"]) - 1) * 100
comparison["leads_change_pct"] = ((comparison["leads_current"] / comparison["leads_previous"]) - 1) * 100
comparison["opportunities_change_pct"] = ((comparison["opportunities_current"] / comparison["opportunities_previous"]) - 1) * 100
comparison["ctr_previous"] = comparison["clicks_previous"] / comparison["impressions_previous"] * 100
comparison["ctr_current"] = comparison["clicks_current"] / comparison["impressions_current"] * 100
comparison["ctr_change_pct"] = ((comparison["ctr_current"] / comparison["ctr_previous"]) - 1) * 100
comparison["click_to_lead_rate_previous"] = comparison["leads_previous"] / comparison["clicks_previous"] * 100
comparison["click_to_lead_rate_current"] = comparison["leads_current"] / comparison["clicks_current"] * 100
comparison["click_to_lead_rate_change_pct"] = ((comparison["click_to_lead_rate_current"] / comparison["click_to_lead_rate_previous"]) - 1) * 100
comparison["leads_to_opportunity_rate_previous"] = comparison["opportunities_previous"] / comparison["leads_previous"] * 100
comparison["leads_to_opportunity_rate_current"] = comparison["opportunities_current"] / comparison["leads_current"] * 100
comparison["leads_to_opportunity_rate_change_pct"] = ((comparison["leads_to_opportunity_rate_current"] / comparison["leads_to_opportunity_rate_previous"]) - 1) * 100

print(comparison)