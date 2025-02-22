## R
library(ggplot2)
library(dplyr)

# Data Ingest and Exploration in R
data <- read.csv("C:/Users/91957/Downloads/Manohar_cleaned_data.csv")

str(data)  # Explore the structure of the dataset

summary(data)  # Summary statistics of the dataset

# Univariate Analysis
# Histogram of Value_nn
ggplot(data, aes(x=Value_nn)) + geom_histogram(binwidth=1, fill="blue", color="black")


# Bar chart of average Value_nn by State
ggplot(data, aes(x=State, y=Value_nn, fill=State)) + 
  geom_bar(stat="summary", fun="mean") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))




# Convert date fields from factor to Date type
data$Time_Period_Start_Date <- as.Date(data$Time_Period_Start_Date, "%d-%m-%Y")


# Univariate Analysis: Line Plot
# Average Value_nn over Time
avg_time_value <- data %>%
  group_by(Time_Period_Start_Date) %>%
  summarise(Average_Value = mean(Value_nn))

# Line plot of average Value_nn over Time
ggplot(avg_time_value, aes(x=Time_Period_Start_Date, y=Average_Value)) +
  geom_line(color="blue") +
  geom_point(color="red") +
  labs(title="Trend of Average Value_nn Over Time", x="Time Period Start Date", y="Average Value_nn")


# Histogram of Value_nn
ggplot(data, aes(x=Value_nn)) +
  geom_histogram(aes(y=..density..), binwidth=1, fill="skyblue", color="black") +
  geom_density(alpha=.2, fill="#FF6666") +
  labs(title="Distribution of Value_nn", x="Value_nn", y="Density") +
  theme_minimal()



# Create a histogram and density plot of Value_nn
ggplot(data, aes(x=Value_nn)) +
  geom_histogram(aes(y=..density..), binwidth=1, fill="skyblue", color="black") + 
  geom_density(alpha=.2, fill="#FF6666") +  
  labs(title="Distribution of Value_nn with Density Overlay",
       x="Value_nn",  
       y="Density") +  
  theme_minimal() 




# Converting dates from factor to Date type
data$Time_Period_Start_Date <- as.Date(data$Time_Period_Start_Date, "%d-%m-%Y")

# Faceted scatter plot by State
ggplot(data, aes(x=Time_Period_Start_Date, y=Value_nn)) +
  geom_point(aes(color=Value_nn), alpha=0.5) +
  facet_wrap(~State) +
  labs(x="Time Period Start Date", y="Value of Symptoms", title="Value of Symptoms Over Time by State") +
  theme_minimal()



# Create a boxplot of Value_nn by State 
ggplot(data, aes(x=State, y=Value_nn, fill=State)) +
  geom_boxplot() +  # Boxplot showing distribution of Value_nn by State
  theme(axis.text.x = element_text(angle=90, vjust=0.5, hjust=1)) +  # Rotate x-axis labels for better visibility
  labs(x="State",  # Label for the x-axis
       y="Value of Symptoms",  # Label for the y-axis
       title="Distribution of Symptom Values by State")  











