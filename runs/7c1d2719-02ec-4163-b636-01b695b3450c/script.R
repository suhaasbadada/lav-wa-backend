library(plotly)
data <- data.frame(x = c(1,2,3), y = c(4,5,6))
fig <- plot_ly(data, x = ~x, y = ~y, type='bar')
htmlwidgets::saveWidget(fig, 'chart.html', selfcontained = TRUE)