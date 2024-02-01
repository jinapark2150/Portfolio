# Jina Park - Data Analyst Portfolio
## About
Hi, I'm Jina! I have recently completed my degree in Mathematics and Statistics. I have developed a strong foundation in the life sciences and a passion for using data to uncover meaningful insights. I am excited to bring my technical and analytical skills to the field of data analysis as an entry-level data specialist.

During my studies, I honed my ability to work with complex data and developed a keen eye for identifying patterns and trends. I also gained experience in laboratory techniques, data management, and statistical analysis, which I believe will be valuable assets in my role as a data specialist.

In my free time, I enjoy exploring new data analysis tools and techniques, and I am always looking for opportunities to expand my knowledge and skills. Whether working on a team or independently, I am driven by the thrill of discovering new insights and the satisfaction of using data to solve complex problems.

This is a repository to showcase skills, share projects, and track my progress in Data Analytics / Data Science related topics.
click on the name of the projects to see my works. Some are raw codes I used for projects and some are pdf files of projects

[CV](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/Projects/loaf) in pdf.

## Personal Projects
### R
#### [One-Way ANOVA Test: Optimizing Concrete Aggregate Selection for Moisture Absorption](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/c35875dad891693cb9c16fef21036cdb7c81f604/Optimizing%20Concrete%20Aggregate%20Selection%20for%20Moisture%20Absorption.R)
* **Purpose**: Determined the most effective concrete aggregate type in terms of moisture absorption, contributing to enhanced material performance in construction projects.
* **Achievements**:
  + Developed and implemented R scripts to analyze data, including checking normality, assessing homogeneity of variances, conducting one-way ANOVA tests, and employing visualizations such as normal QQ plots and residual vs. predicted graphs.
  + Translated outcomes of each technique into comprehensive presentation slides for effective communication.
* **Techniques**: Normality checks, homogeneity assessments, one-way ANOVA tests, normal QQ plot graphs, residual vs. predicted graphs, and Tukey's HSD test.
* **Conclusions**:
  + Identified Type 4 as the most effective concrete aggregate with the least moisture absorption.
  + Found that Types 3 and 5 are not suitable alternatives due to significant differences.
  + Found that Types 1 and 2 can be considered as alternatives, despite Type 1 exhibiting great variation within groups; normality assumption is satisfied.

#### [Two-way ANOVA Test: The Effect of Different Doses of Caffeine on Endurance Performance](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/The%20Effect%20of%20Different%20Doses%20of%20Caffeine%20on%20Endurance%20Performance.r)
* **Purpose**: Conducted an analysis to investigate the correlation between caffeine dosage and individuals' endurance performance.
* **Achievements**:
  + Planned methodology to implement and executed R scripts, employing statistical techniques with a focus on precision and reliability.
  + Translated outcomes of each technique into comprehensive presentation slides for effective communication.
* **Techniques**: Normality checks, homogeneity assessments, two-way ANOVA test, normal QQ plot graphs, residual vs. predicted graphs, and Tukey's HSD test for comparing doses' means.
* **Conclusions**:
  + Established that there is a significant impact of caffeine intake on endurance performance, revealing that caffeine effectively improves individuals; endurance capabilities.
  + Dosage of caffeine may not be a significant effect, as Treatment 1 (0 mg) showed a marked difference from all other treatments according to the results of the Tukey HSD test.
  + Individual cyclists played a crucial role, as indicated by smaller p-values, highlighting that endurance performance variations are more pronounced among cyclists themselves. This emphasizes the personalized nature of the impact of caffeine on endurance.

#### [Effects of Latitude and Elevation on Temperature](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Effects%20of%20Latitude%20and%20Elevation%20on%20Temperature.pdf)
* **Description**: Utilized Bayesian inference to investigate the impact of latitude and elevation on temperature in 16 Texas counties. Collected and analyzed data to establish the relationship between these factors, enabling temperature forecasts.
* **Techniques**: Data Visualization, Ordinary Least Squares (OLS) estimator, Model Selection based on AIC, Maximum Likelihood Estimation, Metropolis Algorithm

#### [Analysis of Diabetes Risk Factors](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Analysis%20of%20Diabetes%20Risk%20Factors.pdf)
* **Description**: This study delves into diabetes, a rapidly increasing health concern with severe consequences. Using data from the National Institute of Diabetes and Digestive and Kidney Diseases on 768 Pima Indian women aged at least 21, advanced statistical techniques were employed. Models were developed through AIC and BIC methods, with variable elimination based on p-values. ANOVA tests, marginal model plots, and multicollinearity checks refined the models, highlighting diabetes pedigree function, BMI, glucose concentration, and insulin concentration as the most influential factors. Diabetes pedigree function exhibited the strongest impact, while insulin concentration had the least effect on diabetes risk.
* **Techniques**: Data cleaning, Data Visualization, Model Development, Model Adequacy Check, Model Selection on AIC and BIC, ANOVA Test, Logistic Regression.



### Python
#### [Star Trek Enterprise Game](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Star%20trek%20enterprise%20game.py)
* **Description**: Developed an interactive game featuring the iconic Star Trek's Enterprise space shuttle engaged in a mission to eliminate Klingon adversaries. Players navigate the space environment, strategically moving the Enterprise to destroy Klingons while facing the challenge of potential damage during encounters.
* **Algorithm**:
  + Random generation of coordinates for 10 stars, 4 Klingons, and 1 Enterprise upon starting the game.
  + Players control the Enterprise's movement using directional commands (East, West, South, North).
  + The Enterprise has random chance of taking random amount of damage within certain range during encounters with Klingons.
  + The Enterprise inflicts a random amount of damage on Klingons when attacking them.
  + Players aim to navigate the Enterprise to eliminate all Klingons without being destroyed.
  + If the Enterprise successfully defeats all Klingons without being destroyed, the game displays a victory message and exits.


## Group Projects
### R
#### [CO2 Exchange Under Wet and Dry Conditions Over Time](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/CO2%20Exchange%20Under%20Wet%20and%20Dry%20Conditions%20Over%20Time.R)
* **Description**: Investigated the optimal conditions for efficient carbon dioxide concentration exchange in plants, aiming to identify key factors influencing the process.
* **Roles and Responsibilities**:
  + Led a team by assigning roles to members, coordinating meeting schedules, distributing reference materials, and maintaining a keen focus on project details.
  + Formulated and executed the methodology, ensuring precision and reliability in the research process.
  + Utilized R scripts and applied advanced statistical techniques, focusing on Timepoint-treatment interaction plots and box plots, followed by ANOVA tests for within-treatment and within-timepoint comparisons.
  + Collaborated with team members to interpret and communicate outcomes derived from each statistical technique.
* **Techniques**:
  + Timepoint-treatment interaction plots and box plots
  + ANOVA test to compare treatments, time-points, and interactions between them
  + Model adequacy checks, including assessments for normality and variance homogeneity
  + Multiple comparisons for detailed analysis of treatment and timepoint variations
* **Conclusions**:
  + The ANOVA test highlighted significant differences in treatments, timepoints, and their interactions.
  + Under dry conditions, treatments T1 and T4 exhibited notable distinctions.
  + In wet conditions, all treatments, except for T1 and T2, displayed significant differences through multiple comparisons.
  + Notably, plants at Timepoint T2 under wet conditions appeared to be the most efficient based on the interaction plot, although no significant difference was found between T1 and T2. Consequently, it can be concluded that either T1 or T2 under wet conditions is potentially the most efficient in terms of CO2 concentration exchange.

#### [Monte Carlo Simulation to Identify Independence and t-distribution](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Monte%20Carlo%20Simulation%20to%20Identify%20Independence%20and%20t-distribution.pdf)
* **Purpose**: Explored the properties of the t-distribution and implemented a Monte Carlo simulation to analyze the independence between variables Z and U under specific conditions
* **Roles and Responsibilities**:
  + Applied knowledge of Student's theorem and properties of the t-distribution to assess the independence of Z and U.
  + Conducted a comprehensive Monte Carlo simulation to gather insights into the behavior of the variables.
  + Collaborated with team members to interpret and communicate the outcomes derived from the simulation and theoretical analyses.
* **Techniques**: Monte Carlo simulation

#### [Multiple Linear Regression of WHO Life Expectancy Data](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Multiple%20Linear%20Regression%20of%20WHO%20Life%20Expectancy%20Data.rmd)
* **Description**: Using 15 years of WHO data from 193 countries, this project employed advanced statistical techniques to identify key determinants of life expectancy. Vaccination rates emerged as the most influential factor in the square root transformed model. Roles included methodology planning, R script execution, and collaborative outcome translation within the team.
* **Techniques**: Data cleaning, Data Visualization, Model Development, Model Adequacy Check, Model Selection on BIC, Model Transformation, ANOVA Test, Multiple Linear Regression

#### [Estimates of Undergraduate Expenses at University of Calgary](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Estimates%20of%20Undergraduate%20Expenses%20at%20University%20of%20Calgary.rmd)
* **Description**: Designed survey instruments, administered, and cleaned the collected data for comprehensive analysis. Employed bootstrap methodology to enhance precision and reliability of approximations in limited sample size

* **Techniques**: Data cleaning, Data Visualization, Model Development, Ratio estimation, Regression estimation, Relative Efficiency, Bootstraps

#### [Prostate Cancer Competing Risk Analysis](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Prostate%20Cancer%20Competing%20Risk%20Analysis.pdf)
* **Description**: 

* **Techniques**: Data cleaning, Data Visualization, Model Development, Ratio estimation, Regression estimation, Relative Efficiency, Bootstraps


#### [Analysis of Competing Risk on Melanoma](https://github.com/jinapark2150/Portfolio_Jina-Park/blob/main/Analysis%20of%20Competing%20Risk%20on%20Melanoma.pdf)
* **Description**: 

* **Techniques**: Data cleaning, Data Visualization, Model Development, Ratio estimation, Regression estimation, Relative Efficiency, Bootstraps
