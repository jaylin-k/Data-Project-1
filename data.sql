SELECT traffic_source, keyword_searched AS search_intent,
  COUNT(DISTINCT session_id) AS total_traffic,
  COUNT(DISTINCT CASE WHEN order_id !='No Order' THEN order_id END) AS total_orders,
  SUM(revenue_amount) AS gross_revenue,
  
  SAFE_DIVIDE(
    COUNT(DISTINCT CASE WHEN order_id != 'No Order' THEN order_id END),
    COUNT(DISTINCT session_id) * 100 
  ) AS conversion_rate,

  COALESCE(
    SAFE_DIVIDE(
    SUM(revenue_amount),
    COUNT(DISTINCT CASE WHEN order_id != 'No Order' THEN order_id END)
    ), 0) AS average_order_value

FROM `data-project-509722.001.001`
GROUP BY 1, 2
ORDER BY gross_revenue DESC;


