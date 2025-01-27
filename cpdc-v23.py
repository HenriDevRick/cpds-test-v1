import tkinter as tk
from tkinter import messagebox

# Define the questions and answers
questions = [
    {
        "question": "The Prioritize component always outputs __________.",
        "options": [
            "a) on arbitrary number of offers",
            "b) top 1 offer",
            "c) top 3 offers",
            "d) all eligible offers"
        ],
        "answer": "d"
    },
    {
        "question": "An Adaptive model component in a decision strategy can output ____________.",
        "options": [
            "a) an optimized strategy",
            "b) the customer's propensity to accept an action",
            "c) the number of customers eligible for an action",
            "d) an action"
        ],
        "answer": "b"
    },
    {
        "question": "A data scientist and an application developer must configure a chatbot to improve customer service response time. The application developer created the digital messaging channel. \n What is the next step for the data scientist? \n",
        "options": [
            "a) Create a new text prediction and associate it with the digital messaging channel that the application developer creates.",
            "b) Create and train a new text prediction and inform the application developer.",
            "c) Modify pySystemEntities model to meet business needs, and then associate it with the digital messaging channel that the application developer created.",
            "d) Train the text prediction that the system generates."
        ],
        "answer": "d"
    },
    {
        "question": "A coffee company wants to create a data set that includes mock up customer address information and the likelihood to churn. \n Which method is available to populate these fields? \n",
        "options": [
            "a) Bayesian",
            "b) Propensity",
            "c) Expression",
            "d) Import"
        ],
        "answer": "c"
    },
    {
        "question": "What is entity extraction in NLP?",
        "options": [
            "a) The process of identifying the subject of a sentence",
            "b) The process of identifying the sentiment of a sentence",
            "c) The process of identifying the action that a user intends to take based on their input",
            "d) The process of identifying specific entities or objects mentioned in a sentence, such as people, places, and organizations"
        ],
        "answer": "d"
    },
    {
        "question": "U+ Bank introduces a new credit card that has no historical customer behavior data. U+ Bank wants to offer this credit card on the personalized web portal. \n Given the scenario, which rule type must you use? \n ",
        "options": [
            "a) Adaptive model",
            "b) Pega machine learning model",
            "c) When rule",
            "d) Decision table"
        ],
        "answer": "a"
    },
    {
        "question": "As a data scientist, you want to export the model and predictor data for the Credit Cards group from the Grow business issue for further analysis. You are tasked to modify the data flow to select the correct data. Match the data flow component to the function it achieves. \n 1. Source component \n 2. Compose component \n 3. Filter component \n 4. Destination component \n \n A. Retrives data. \n B. Stores the results the data flow. \n C. Selects a subset of the records. \n D. Combine data from multiple sources. \n",
        "options": [
            "a) 1-B ,2-A ,3-D ,4-C ",
            "b) 1-C ,2-D ,3-A ,4-B",
            "c) 1-B ,2-D ,3-C ,4-A",
            "d) 1-D ,2-B ,3-C ,4-A"
        ],
        "answer": "c"
    },
    {
        "question": " What is Adaptive Analytics?",
        "options": [
            "a) A statistical technique for analyzing data",
            "b) A machine learning algorithm for predicting future outcomes",
            "c) A flexible approach to data analysis that can adapt to changing business needs and data environments",
            "d) A software application for managing business workflows"
        ],
        "answer": "c"
    },
    {
        "question": "U+ Bank wants to offer a 10% discount for customers whose CLV value is higher than 400. \n Which strategy component should you use to meet the new requirement? \n ",
        "options": [
            "a) Group by",
            "b) Prioritize",
            "c) Filter",
            "d) Set property"
        ],
        "answer": "d"
    },
    {
        "question": "What are the benefits of using Predictive Analytics?",
        "options": [
            "a) Faster insights from data",
            "b) More accurate predictions",
            "c) Increased agility in responding to changing business needs",
            "d) Improved customer service"
        ],
        "answer": "b"
    },
    {
        "question": "You have created a predictive model using R and have exported it to Predictive Model Markup Language (PMML). \n Which component in a decision strategy do you use to leverage the PMML model? \n ",
        "options": [
            "a) Third-party model",
            "b) Predictive model",
            "c) Scorecard model",
            "d) Decision tree"
        ],
        "answer": "b"
    },
    {
        "question": "The purpose of predictions is to______________",
        "options": [
            "a) monitor the success rate of individual actions",
            "b) add predictors to adaptive models",
            "c) build adaptive models",
            "d) add best data scientist practices to adaptive models"
        ],
        "answer": "d"
    },
    {
        "question": "U+ Bank, a retail bank, recently implemented a project in which credit card offers are presented to qualified customers when they log in to the web self-service portal. The bank does not want any bias except to satisfy the eligibility condition Age >=18. \n As a decisioning consultant, how do you configure the ethical bias policy to allow a minimum bias on age? \n ",
        "options": [
            "a) 0.7 Gini",
            "b) 0.1 Gini",
            "c) No detection",
            "d) 0 Gini"
        ],
        "answer": "b"
    },
    {
        "question": "What happens when you increase the performance threshold setting of an Adaptive Model rule?",
        "options": [
            "a) The number of active predictors increases.",
            "b) The correlation threshold decreases.",
            "c) The performance of the model is increased.",
            "d) The number of active predictors may decrease."
        ],
        "answer": "b"
    },
    {
        "question": "With the open-source GitHub repository Pega Data Scientist Tools, you can ______________.",
        "options": [
            "a) visualize the performance of a predictor",
            "b) analyze your data in SQL",
            "c) build XGBoost models",
            "d) upload predictive models to Prediction Studio"
        ],
        "answer": "a"
    },
    {
        "question": "Which of the following is NOT a benefit of using Pega Process AI?",
        "options": [
            "a) Increased efficiency and productivity",
            "b) Improved customer satisfaction",
            "c) Reduced costs",
            "d) Enhanced data security"
        ],
        "answer": "d"
    }, {
        "question": "Adaptive models can learn without historical evidence. \n What is the starting propensity of every action?",
        "options": [
            "a) 0.25",
            "b) 0.5",
            "c) 1",
            "d) 0"
        ],
        "answer": "b"
    },
    {
        "question": "What is data cleansing in Predictive Analytics?",
        "options": [
            "a) Removing duplicate or inconsistent data",
            "b) Removing irrelevant data",
            "c) Removing confidential data",
            "d) All the above"
        ],
        "answer": "a"
    },
    {
        "question": "U+ Bank presents a personalized credit card offer to its customers when they log in to their accounts on the website. The Predict Web Propensity prediction calculates the likelihood of a customer clicking on the credit card offer banner. \n In Pega Customer Decision Hub™, what does the Clicked response label signify in this context? \n ",
        "options": [
            "a) The customer showed interest in the credit card offer.",
            "b) The customer ignored the credit card offer.",
            "c) The customer received an email with the credit card offer.",
            "d) The customer did not respond to the offer."
        ],
        "answer": "a"
    },
    {
        "question": "What is provided as input to a predictive model component by the strategy?",
        "options": [
            "a) Customer data",
            "b) The strategy outcome",
            "c) Performance data",
            "d) Proposition identifier"
        ],
        "answer": "a"
    },
    {
        "question": "Which decision component allows you to monitor the real-time performance of a third-party Churn Model?",
        "options": [
            "a) PMML Model",
            "b) Scorecard Model",
            "c) Predictive Model",
            "d) Adaptive Model"
        ],
        "answer": "b"
    },
    {
        "question": "The Adaptive Model component in a strategy computes __________.",
        "options": [
            "a) a propensity value for each action",
            "b) a single accept rate for all actions",
            "c) a unique accept rate for each action",
            "d) a single propensity value for all actions"
        ],
        "answer": "d"
    },
    {
        "question": "Which of the following is NOT a use case for Pega Process AI?",
        "options": [
            "a) Fraud detection and prevention",
            "b) Customer service automation",
            "c) Sales forecasting and analysis",
            "d) Supply chain optimization"
        ],
        "answer": "c"
    },
    {
        "question": "Pega Customer Decision Hub™ uses the P*C*V*L arbitration formula to select the next best action for each customer. \n Which description best describes the purpose of the formula? \n ",
        "options": [
            "a) To balance customer needs with business objectives.",
            "b) To ensure that the customer is always given the best offer, regardless of the business objective.",
            "c) To provide insight into business processes.",
            "d) To ensure that every customer receives the same action."
        ],
        "answer": "a"
    },
    {
        "question": "Why is leaving the default settings of an adaptive model unchanged important?",
        "options": [
            "a) Using the default settings is based on best practices.",
            "b) Changing the settings is not a task for a data scientist.",
            "c) Changing the settings does not effect model performance.",
            "d) Adaptive Decision Manager adjusts the settings automatically adjusted during adaptive learning."
        ],
        "answer": "a"
    },
    {
        "question": "Which of the following is a technique used in NLP for text classification?",
        "options": [
            "a) SVM (Support Vector Machines)",
            "b) K-Means",
            "c) Random Forest",
            "d) Naive Bayes"
        ],
        "answer": "d"
    },
    {
        "question": "What is predictor importance in the context of machine learning?",
        "options": [
            "a) The importance of each predictor in calculating propensity.",
            "b) The importance of each predictor to the business team.",
            "c) The importance of each predictor across all models.",
            "d) The importance of each decision in calculating propensity."
        ],
        "answer": "a"
    },
    {
        "question": "What is the importance of data normalization in Predictive Analytics?",
        "options": [
            "a) It ensures that all data is in the same format",
            "b) It ensures that all data is relevant to the model",
            "c) It ensures that all data is accurate",
            "d)  It ensures that all data is on the same scale"
        ],
        "answer": "d"
    },
    {
        "question": "What is the purpose of the Combiner function in the scorecard?",
        "options": [
            "a) To create complex predictor field expressions.",
            "b) To apply a data transform to run the scorecard for different customers.",
            "c) To set the Cutoff value to distinguish potential churners from loyal customers.",
            "d) To select a method to calculate the score."
        ],
        "answer": "d"
    },
    {
        "question": "In a decision strategy, which component is required to enable access to primary customer properties?",
        "options": [
            "a) None; customer properties are available.",
            "b) Customer Import",
            "c) Data Import",
            "d) Set Property"
        ],
        "answer": "a"
    },
    {
        "question": "In the delta view in Visual Business Director, what does the red-colored cone indicate?",
        "options": [
            "a) The source data value is too small",
            "b) The source data value is smaller than the reference data value",
            "c) The source data value is larger than the reference data value",
            "d) The source data value is too large"
        ],
        "answer": "b"
    },
    {
        "question": "An online store is interested in increasing its revenues from cross-selling and wants to predict the acceptance rate of the offers presented on their website. \n A customer's propensity to accept an offer increases when ___________________. \n",
        "options": [
            "a) similar offers were rejected by the customer",
            "b) similar offers were accepted by the customer",
            "c) the offer was rejected by similar customers",
            "d) the offer was accepted by similar customers"
        ],
        "answer": "c"
    },
    {
        "question": "What is the importance of data quality in Adaptive Analytics?",
        "options": [
            "a) It ensures accurate and reliable insights",
            "b) It speeds up the data analysis process",
            "c) It makes it easier to implement machine learning algorithms",
            "d) It allows for more complex data visualizations"
        ],
        "answer": "a"
    },
    {
        "question": "When executing a decision strategy, the dotted line arrow in a decision strategy means data is __________.",
        "options": [
            "a) copied to the component the arrow points to",
            "b) referenced by the component the arrow originates from",
            "c) referenced by the component the arrow points to",
            "d) copied to the component the arrow originates from"
        ],
        "answer": "b"
    },
    {
        "question": "A company wants to capture the sentiment of relevant Twitter messages to allow its customer service representatives to concentrate only on the negative messages. \n Sentiment refers to the general attitude of the author towards a subject and can be ____________. \n ",
        "options": [
            "a) Defensive",
            "b) Absent",
            "c) Offensive",
            "d) Positive"
        ],
        "answer": "c"
    },
    {
        "question": "Which property is automatically recomputed for each decision component?",
        "options": [
            "a) Order",
            "b) Rank",
            "c) Propensity",
            "d) Priority"
        ],
        "answer": "b"
    },
    {
        "question": "To enable an assessment of its reliability the adaptive model produces four outputs: propensity, performance, evidence and positives. The Performance of an adaptive model that has not collected any evidence yet is______.",
        "options": [
            "a) 75",
            "b) 100",
            "c) 0",
            "d) 50"
        ],
        "answer": "d"
    },
    {
        "question": "U+ Bank, a retail bank, offers the Standard card, the Rewards card and the Rewards Plus card to its customers. The bank wants to display the banner for the offer that each customer is most likely to click; therefore, their Arbitration uses Propensity from the AI models. \n If you are debugging the Next-BestAction decision strategy, which strategy component will show you if the result of the Arbitration is correct? \n ",
        "options": [
            "a) Group By",
            "b) Set Property",
            "c) Prioritize",
            "d) Filter"
        ],
        "answer": "c"
    },
    {
        "question": "In a Prioritize component, the best action can be determined based on the value of __________.",
        "options": [
            "a) Customer, Value",
            "b) Propensity",
            "c) Average Margin",
            "d) Customer.Income"
        ],
        "answer": "c"
    },
    {
        "question": "To implement eligibility criteria you can use a ____________ component.",
        "options": [
            "a) Decision Table",
            "b) Switch",
            "c) Group by",
            "d) Segment"
        ],
        "answer": "a"
    },
    {
        "question": "In a decision strategy, to select the proposition with the highest propensity, you use a __________.",
        "options": [
            "a) Priorities component, and sort propensity from highest to lowest",
            "b) Priorities component, and sort propensity from lowest to highest",
            "c) Switch component, and sort propensity from lowest to highest",
            "d) Switch component, and sort propensity from highest to lowest"
        ],
        "answer": "d"
    },
    {
        "question": "U+ Telecom uses predictive analytics for case management. As a data scientist, you have created a predictive model based on recent historical company data and have placed the new model in shadow mode. \n Which statement is true about the new predictive model? \n ",
        "options": [
            "a) The active model and the new model affect business outcomes.",
            "b) The new model affects business outcomes.",
            "c) The new model does not affect business outcomes.",
            "d) The active model does not affect business outcomes."
        ],
        "answer": "c"
    },
    {
        "question": "What is the key characteristic that Next-Best-Action must consider to satisfy customer needs?",
        "options": [
            "a) Service",
            "b) Fraud",
            "c) Mobility",
            "d) Relevancy"
        ],
        "answer": "d"
    },
    {
        "question": "To configure an adaptive model, the responses that indicate specific customer behavior must be identified. \n What types of behavior need to be identified? \n",
        "options": [
            "a) Any behavior",
            "b) Positive and negative behavior",
            "c) Positive, neutral, and negative behavior",
            "d) Positive behavior only"
        ],
        "answer": "b"
    },
    {
        "question": "What is data stewardship?",
        "options": [
            "a) The process of managing an organization's data",
            "b) The process of using an organization's data",
            "c) The process of storing an organization's data",
            "d) The process of analyzing an organization's data"
        ],
        "answer": "a"
    },
    {
        "question": "When compared to a Predictive Model, an Adaptive Model is different as it _______________.",
        "options": [
            "a) cannot perform a spectrum model calculation",
            "b) considers both symbolic and numeric predictors",
            "c) uses customer properties as predictors",
            "d) uses predictive binning"
        ],
        "answer": "a"
    },
    {
        "question": ". What role do customizable thresholds play in managing notifications in Prediction Studio?",
        "options": [
            "a) Data Scientists use customizable thresholds to select relevant types of notifications.",
            "b) Customizable thresholds determine the order in which notifications are displayed.",
            "c) Customizable thresholds define when specific types of notifications are triggered.",
            "d) Data Scientists use customizable thresholds to adjust the color scheme of notifications."
        ],
        "answer": "c"
    },
    {
        "question": "When developing a predictive model, a valid data type for a predictor is _______________.",
        "options": [
            "a) Integer",
            "b) Numeric",
            "c) Number",
            "d) Character"
        ],
        "answer": "b"
    },
    {
        "question": "The Actuals data set, that can be inspected with Visual Business Director, contains ____________",
        "options": [
            "a) real-time customer interactions data",
            "b) the delta of the source data set and the reference data set",
            "c) customer data",
            "d) proposition data"
        ],
        "answer": "a"
    },
    {
        "question": "The system continuously monitors the predicting power of every predictor. \n When does the system activate a previously dormant predictor? \n ",
        "options": [
            "a) When the data scientist activates the predictor.",
            "b) When the number of responses improves above a threshold.",
            "c) When the predictive power of the predictor drops below a threshold.",
            "d) When the predictive power of the predictor improves above a threshold."
        ],
        "answer": "d"
    },
    {
        "question": "An adaptive model instance is created when you________",
        "options": [
            "a) Save the Adaptive model rule",
            "b) Open the Adaptive model management landing page",
            "c) Restart the Adaptive Decision Manager Service",
            "d) Execute a strategy containing the adaptive model component"
        ],
        "answer": "d"
    },
    {
        "question": "What is the support of an association rule?",
        "options": [
            "a) The proportion of transactions in the dataset that contain all items in the rule",
            "b) The proportion of transactions in the dataset that contain at least one item in the rule",
            "c) The proportion of transactions in the dataset that do not contain any items in the rule",
            "d) The proportion of items in the dataset that are in the rule"
        ],
        "answer": "a"
    },
    {
        "question": "A telecommunications company wants to monitor Twitter data and generate an adequate response. \n Text analytics detects proper nouns such as names, dates, and places as _______ \n ",
        "options": [
            "a) Objects",
            "b) Entities",
            "c) Subjects",
            "d) Topics"
        ],
        "answer": "b"
    },
    {
        "question": "Which group is responsible for providing oversight and review processes for all predictive models used by the organization before their launch in a Pega Customer Decision Hub™ project?",
        "options": [
            "a) Model Governance",
            "b) Data Engineering",
            "c) Marketing Ops",
            "d) Data Scientists"
        ],
        "answer": "a"
    },
    {
        "question": "Which statement best describes the goal of the next best action?",
        "options": [
            "a) To ensure that every customer receives the same action.",
            "b) To provide insight into business processes.",
            "c) To ensure that the customer always receives given a desirable offer.",
            "d) To balance customer needs with business objectives."
        ],
        "answer": "d"
    },
    {
        "question": "How can Adaptive Analytics models be deployed in production environments?",
        "options": [
            "a) Manually copying and pasting the code into a production system",
            "b) Ignoring production deployment and only using models for offline analysis",
            "c) Only deploying models in a sandbox environment",
            "d) Using a software development process to test and deploy models"
        ],
        "answer": "d"
    },
    {
        "question": "When developing a predictive model, the outcome value of a continuous model type can represent _________________.",
        "options": [
            "a) the purchase value of an offer",
            "b) customer loan default",
            "c) customer churn",
            "d) acceptance of an offer"
        ],
        "answer": "a"
    },
    {
        "question": "What are association rules in data mining?",
        "options": [
            "a) Rules that describe the relationships between variables in a dataset",
            "b) Rules that describe the relationships between transactions in a dataset",
            "c) Rules that describe the relationships between features in a dataset",
            "d) Rules that describe the relationships between models in a dataset"
        ],
        "answer": "b"
    },
    {
        "question": "Prediction Studio supports keyword-based topic detection, model-based topic detection and the combination of these. \n When using machine learning, ______________________________. \n",
        "options": [
            "a) keywords have a higher impact on the model than the training data",
            "b) the most keywords function as positive features",
            "c) the keywords are ignored",
            "d) keywords are measured, and those with high impact are ignored"
        ],
        "answer": "b"
    },
    {
        "question": "U+, a retail bank, offers the Standard card, the Rewards card and the Rewards Plus card to its customers. The bank wants to display the banner for the offer that each customer is most likely to click; therefore, their Arbitration uses Propensity from the AI models. \n If you are debugging the Next-Best-Action decision strategy, which strategy component will show you if the result of the Arbitration is correct? \n ",
        "options": [
            "a) Group by",
            "b) Set property",
            "c) Filter",
            "d) Prioritize"
        ],
        "answer": "d"
    },
    {
        "question": "In Pega Customer Decision Hub™, adaptive models calculate propensities that support the optimization of customer interactions. \n How does the system support explanations of the factors that drive a single propensity calculation? \n ",
        "options": [
            "a) By showing the current prioritization of next-best-action results.",
            "b) By offering built-in support for calculating global predictor importance.",
            "c) By exporting the ADM predictor importance report for further analysis.",
            "d) By providing local explanations of the decisions made by Customer Decision Hub."
        ],
        "answer": "d"
    },
    {
        "question": "U+ Bank presents a personalized credit card offer to its customers when they log in to their accounts on the website. The Predict Web Propensity prediction calculates the likelihood of a customer clicking on the credit card offer banner.",
        "options": [
            "a) The offer is displayed again with a different design.",
            "b) The customer's account is locked.",
            "c) The system automatically accepts the offer on behalf of the customer.",
            "d) Pega Customer Decision Hub™ records a NoResponse outcome is recorded."
        ],
        "answer": "d"
    },
    {
        "question": "In a decision strategy, which component is required to enable access to proposition properties?",
        "options": [
            "a) Proposition Data",
            "b) Data Include",
            "c) Data Join",
            "d) Property Import"
        ],
        "answer": "a"
    },
    {
        "question": "What is ensemble learning in Predictive Analytics?",
        "options": [
            "a) A technique for combining the predictions of multiple models",
            "b) A technique for training a single model on multiple datasets",
            "c) A technique for automatically selecting the best algorithm for a given problem",
            "d) A technique for validating a model using multiple datasets"
        ],
        "answer": "a"
    },
    {
        "question": "A large online store wants to adapt to changing customer behavior but does not want to be distracted by fads. Adaptive models can help accomplish both business objectives. \n Which statement about adaptive models is correct? \n",
        "options": [
            "a) Adaptive models perform a continuous model calculation.",
            "b) Adaptive models require no historical data to get started.",
            "c) Adaptive models are regression models.",
            "d) Adaptive models require underlying predictive models."
        ],
        "answer": "b"
    },
    {
        "question": "What is Pega Process AI?",
        "options": [
            "a) A process automation tool",
            "b) An AI-powered tool for process optimization and automation ",
            "c) A machine learning tool for predicting process outcomes",
            "d) A tool for monitoring process performance"
        ],
        "answer": "b"
    },
    {
        "question": "When selecting the list of predictors for an adaptive model you should…",
        "options": [
            "a) select up to a maximum of 500 predictors",
            "b) select at least one data property",
            "c) always use numeric type for integer properties",
            "d) consider a wide range of properties"
        ],
        "answer": "a"
    },
    {
        "question": "What is the difference between classification and regression in Predictive Analytics?",
        "options": [
            "a) Classification is used for predicting continuous outcomes, while regression is used for predicting categorical outcomes",
            "b) Classification is used for predicting categorical outcomes, while regression is used for predicting continuous outcomes",
            "c) Classification and regression are the same thing",
            "d) Neither classification nor regression are used in Predictive Analytics"
        ],
        "answer": "b"
    },
    {
        "question": "U+ Bank promotes credit card offers on its website and uses Pega Customer Decision Hub™ to personalize the offer for every customer. Now, the bank wants to lower the number of customers that leave the bank by showing a proactive retention offer to high churn risk customers instead. As an NBA analyst, you are tasked with creating a new applicability setting to comply with the new business rule. \n Which business issue or issues do you modify? \n ",
        "options": [
            "a) Both the Sales issue and the Retention issue",
            "b) Only the Sales issue ",
            "c) Only the Retention issue"
        ],
        "answer": "a"
    },
    {
        "question": "U+ Bank relies on a text prediction to route incoming emails to the correct department. \n To detect an account number in the text, the text prediction uses ____________. \n",
        "options": [
            "a) an entity extraction model",
            "b) a language model",
            "c) a sentiment model",
            "d) a topic model"
        ],
        "answer": "a"
    },
    {
        "question": "What is the role of an IT steering committee?",
        "options": [
            "a) To oversee an organization's IT strategy and investments",
            "b) To oversee an organization's IT security",
            "c) To oversee an organization's IT accessibility",
            "d) To oversee an organization's IT availability"
        ],
        "answer": "a"
    },
    {
        "question": "With which component in Next-Best-Action Designer can you define the business structure for your organization by grouping actions into categories such as Acquire and Grow?",
        "options": [
            "a) Arbitration",
            "b) Engagement Policy",
            "c) Taxonomy",
            "d) Constraints"
        ],
        "answer": "c"
    },
    {
        "question": "Which of the following is NOT a use case for NLP in Pega?",
        "options": [
            "a) Sentiment analysis",
            "b) Text classification",
            "c) Speech recognition",
            "d) Entity extraction"
        ],
        "answer": "c"
    },
    {
        "question": "The output of a predictive model is accessible by other components in the strategy via a property called ____________",
        "options": [
            "a) pxSegment",
            "b) pyOutcome",
            "c) pxRank",
            "d) pyPropensity"
        ],
        "answer": "a"
    },
    {
        "question": "U+ Telecom uses predictive analytics in its retention strategy. You have created a predictive model based on recent historical company data and have placed the new model in shadow mode. \n Which statement is true about the new predictive model? \n ",
        "options": [
            "a) The active model and the new model affect business outcomes.",
            "b) The new model affects business outcomes.",
            "c) The new model does not affect business outcomes.",
            "d) The active model does not affect business outcomes."
        ],
        "answer": "d"
    },
    {
        "question": "As a decisioning consultant, you are tasked with configuring the ethical bias policy. \n Which context do you need to select to add bias fields? \n",
        "options": [
            "a) Action",
            "b) Action group",
            "c) Treatment",
            "d) Customer"
        ],
        "answer": "d"
    },
    {
        "question": "Who configures the outbound schedule, updates strategy logic, and optimizes customer interactions across all channels in a Pega Customer Decision Hub™ implementation?",
        "options": [
            "a) Data Engineering",
            "b) CDH Implementation team",
            "c) Data Scientists",
            "d) Marketing Ops"
        ],
        "answer": "d"
    },
    {
        "question": "Which of the following statements is true when describing Predictive Model Markup Language (PMML) models?",
        "options": [
            "a) PMML models must be converted before they can be used.",
            "b) PMML models are specialized models created by Predictive Analytic Director.",
            "c) PMML-compliant models can be used in the same strategies as Pega’s predictive models.",
            "d) PMML-compliant models cannot be used in the same strategies as Pega’s predictive models."
        ],
        "answer": "c"
    },
    {
        "question": "U+ Insurance uses a fraud model to route suspicious claims to an expert for closer inspection. In the case type that processes incoming claims, what type of process step does AI support?",
        "options": [
            "a) Assignment step",
            "b) Change to a stage step",
            "c) Decision step",
            "d) Approve/Reject step"
        ],
        "answer": "c"
    },
    {
        "question": "What is the purpose of using a validation data set when updating a predictive model by using Machine Learning Operations (MLOps)?",
        "options": [
            "a) To compare the performance of the updated model to the active model.",
            "b) To test the updated model in a development environment.",
            "c) To deploy the updated model to a staging environment.",
            "d) To monitor the updated model in a production environment."
        ],
        "answer": "a"
    },
    {
        "question": "Which statement about the PMML standard is correct?",
        "options": [
            "a) The PMML standard facilitates the exchange of scores between applications.",
            "b) The PMML standard is a proprietary standard.",
            "c) The PMML standard facilitates the exchange of models between applications.",
            "d) You can only use the PMML standard to describe tree, scorecard, and regression models."
        ],
        "answer": "c"
    },
    {
        "question": "When defining outcomes for an Adaptive Model you must define",
        "options": [
            "a) behavior values to be ignored",
            "b) only negative behavior values",
            "c) positive, negative and neutral behavior values",
            "d) one or more positive behavior values"
        ],
        "answer": "d"
    },
    {
        "question": "A legal firm wants to use text analytics for easier and faster access to information to help with compliance related issues. The legal firm needs a taxonomy of legal concepts. What is a taxonomy?",
        "options": [
            "a) A list of valid categories",
            "b) A sentiment analysis model",
            "c) The output of an expert survey",
            "d) A list of business rules"
        ],
        "answer": "a"
    },
    {
        "question": "Which statement about the expected performance of a binary model is correct?",
        "options": [
            "a) The expected performance is an optional field for binary models.",
            "b) You set the expected performance before deploying the model.",
            "c) The system automatically calculates the expected performance."
        ],
        "answer": "a"
    },
    {
        "question": "The decision components used on the strategy canvas can be individually configured. Which function is available when configuring the Group By component?",
        "options": [
            "a) Multiply",
            "b) Divide",
            "c) Average",
            "d) True if Some"
        ],
        "answer": "c"
    },
    {
        "question": "How can the effectiveness of Adaptive Analytics models be measured?",
        "options": [
            "a) By comparing model predictions to actual outcomes",
            "b) By running the model on more data",
            "c) By adjusting the model parameters",
            "d) By only measuring accuracy at the beginning of the project"
        ],
        "answer": "a"
    },
    {
        "question": "A contact center application recommends three actions for a customer. The business team wants to know the possible ways in which these actions can be ordered so that the contact center agent can discuss one proposition at a time, starting from the top. As a strategy designer, if you use a Prioritize component to order the actions, what are your options?",
        "options": [
            "a) In a random order",
            "b) In ascending or in descending order based on a numerical value",
            "c) In the order in which they are displayed in the strategy canvas",
            "d) In the order controlled by the contact center agent"
        ],
        "answer": "c"
    },
    {
        "question": "Which statement about Pega Process AI is correct?",
        "options": [
            "a) Pega Process AI lets you design strategies.",
            "b) Pega Process AI lets you use your own predictive models.",
            "c) Pega Process AI is restricted to external models."
        ],
        "answer": "b"
    },
    {
        "question": "The Pega Customer Decision Hub delivers the Next-Best-Action consistently through multiple channels. To which channel does this apply?",
        "options": [
            "a) Newspaper",
            "b) Mobile",
            "c) Television",
            "d) Billboard"
        ],
        "answer": "b"
    },
    {
        "question": "U+ Insurance wants straight-through processing of claims with a low fraud risk. As a data scientist, you create a prediction that calculates the probability that a claim is fraudulent. What type of prediction do you create?",
        "options": [
            "a) Customer Decision Hub",
            "b) Case management",
            "c) Text analytics",
            "d) Strategic"
        ],
        "answer": "b"
    },
    {
        "question": "A company wants to capture the sentiment of messages to allow its customer service representatives to focus on only the negative messages. Sentiment refers to the general attitude of the author towards a subject and can be _______________.",
        "options": [
            "a) absent",
            "b) offensive",
            "c) negative",
            "d) defensive"
        ],
        "answer": "c"
    },
    {
        "question": "What is a risk mitigation plan?",
        "options": [
            "a) A plan for avoiding risks",
            "b) A plan for reducing the impact of risks",
            "c) A plan for accepting risks",
            "d) A plan for transferring risks to another party"
        ],
        "answer": "b"
    },
    {
        "question": "What are some common challenges with data management in Adaptive Analytics? (Choose three)",
        "options": [
            "a) Data privacy and security concerns",
            "b) Inaccurate or incomplete data",
            "c) Limited availability of data",
            "d) Lack of analytical tools"
        ],
        "answer": "abc"
    },
    {
        "question": "A data scientist must create an entity extraction model to recognize bank account numbers for U+ bank. The account numbers follow a strict pattern: 2 letters followed by 10 digits. What is the best choice for the data scientist to make to implement this requirement?",
        "options": [
            "a) Create an entity extraction model based on Ruta script.",
            "b) Create a new Ruta script-based entity in the pySystemEntities model.",
            "c) Use the out-of-the-box pySystemEntities model, which contains an entity extraction model specific for this requirement.",
            "d) Create an entity extraction model based on machine learning, and then train it with a dataset that contains emails from customers."
        ],
        "answer": "a"
    },
    {
        "question": "Adaptive model predictors are selected from the____________.",
        "options": [
            "a) customer profile",
            "b) communication channel",
            "c) similar propositions",
            "d) proposition profile"
        ],
        "answer": "a"
    },
    {
        "question": "When a new component is added to the strategy canvas, its Rank value will be __________.",
        "options": [
            "a) One higher than the current highest Rank",
            "b) 0",
            "c) Not set",
            "d) 1"
        ],
        "answer": "b"
    },
    {
        "question": "A large online store wants to adapt to changing customer behavior, and at the same time does not want to get earned away by every next hype in the market. Adaptive models can help accomplish both business objectives. Which statement about adaptive models is correct?",
        "options": [
            "a) Adaptive models perform a spectrum model calculation.",
            "b) Adaptive models perform a scoring model calculation.",
            "c) Adaptive models require underlying predictive models.",
            "d) Adaptive models are regression models."
        ],
        "answer": "a"
    },
    {
        "question": "You are a company with a new and unique product, and you want to offer it to the right customer. Given the scenario, which rule type should you use?",
        "options": [
            "a) Scorecard",
            "b) Adaptive Model",
            "c) Predictive Model",
            "d) Decision Table"
        ],
        "answer": "d"
    },
    {
        "question": "What is overfitting in Predictive Analytics?",
        "options": [
            "a) When a model is too simple and does not capture all relevant data",
            "b) When a model is too complex and captures noise in the data",
            "c) When a model is not accurate enough",
            "d) When a model is too accurate and cannot be trusted"
        ],
        "answer": "b"
    },
    {
        "question": "What is autocorrelation in time series analysis?",
        "options": [
            "a) A measure of how correlated two variables are",
            "b) A measure of how correlated a variable is with its own past values",
            "c) A measure of how correlated a variable is with its own future values",
            "d) A measure of how correlated two time series are"
        ],
        "answer": "b"
    },
    {
        "question": "Configuring an adaptive model involves selecting the potential predictors. What is the best number of potential predictors for an adaptive model?",
        "options": [
            "a) At least 100 fields to reach an acceptable level of model performance.",
            "b) Up to 100 fields to limit the impact on model speed.",
            "c) As many available fields that can contribute to the predictive power of the model.",
            "d) All fields that have been predictive in the past."
        ],
        "answer": "c"
    },
    {
        "question": "What is the primary purpose of the Engagement Policy component in Next-Best-Action Designer?",
        "options": [
            "a) To implement contact limits and constraints.",
            "b) To determine when and where the next best actions initiate.",
            "c) To configure the prioritization of actions.",
            "d) To define rules for which actions customers qualify for."
        ],
        "answer": "d"
    },
    {
        "question": "To configure an adaptive model, you identify the responses that indicate specific customer behavior. What types of behavior do you specify?",
        "options": [
            "a) Positive behavior only",
            "b) Any behavior",
            "c) Positive and negative behavior",
            "d) Positive, neutral, and negative behavior"
        ],
        "answer": "c"
    },
    {
        "question": "What type of a predictor can you use in an adaptive model?",
        "options": [
            "a) Symbolic",
            "b) Page Type",
            "c) Logical",
            "d) Customer identifiers"
        ],
        "answer": "a"
    },
    {
        "question": "What is the purpose of the business operations environment (BOE) in a one-to-one customer engagement project that uses Pega Customer Decision Hub™?",
        "options": [
            "a) To collect customer responses.",
            "b) To add precalculated model scores to the data model.",
            "c) To add precalculated model scores to the data model.",
            "d) To create, modify, and test business artifacts and conduct simulations."
        ],
        "answer": "d"
    },
    {
        "question": "Which two factors do you inspect to assess the general health of the adaptive models in Prediction Studio? (Choose Two.)",
        "options": [
            "a) Model transparency",
            "b) Insights",
            "c) Performance of the models",
            "d) Number of decisions"
        ],
        "answer": "ac"
    },
    {
        "question": "Which rule is used to upload a Predictive Modeling Markup Language (PMML) file that contains a Tree model type?",
        "options": [
            "a) Scorecard",
            "b) Decision tree",
            "c) Predictive model",
            "d) Third-party Model"
        ],
        "answer": "c"
    },
    {
        "question": "U+ Bank presents a personalized credit card offer to its customers when they log in to their accounts on the website. The Predict Web Propensity prediction calculates the likelihood of a customer clicking on the credit card offer banner. How does Pega Customer Decision Hub™ determine which credit card to offer to a customer who is eligible for multiple credit cards, based on the Predict Web Propensity prediction?",
        "options": [
            "a) The customer receives the option to choose any credit card.",
            "b) The system offers the credit card with the highest Clicked propensity.",
            "c) The system offers the credit card with the longest promotional period.",
            "d) The system offers the credit card with the highest annual fee."
        ],
        "answer": "b"
    },
    {
        "question": "What is the purpose of shadow mode when you deploy a new model?",
        "options": [
            "a) To test the new model with a sample of data.",
            "b) To monitor the performance of the new model in a production environment before you deploy it as an active model.",
            "c) To deploy the new model immediately as an active model.",
            "d) To drive the prediction by both the active model and the new model."
        ],
        "answer": "b"
    },
    {
        "question": "An application developer and a data scientist are working together on a chatbot project. They want the chatbot to detect that the customer wants to change the account home address. To achieve this goal, the chatbot must: - Detect the topic of the message - Run the correct case type - Extract 2 entities: new address and account number. What main tasks must they do to achieve this business scenario? (Choose Three)",
        "options": [
            "a) The application developer creates the digital messaging channel.",
            "b) The application developer creates the case type and designs the conversation flow.",
            "c) The data scientist uses the entity extraction model from pySystemEntities model and trains the topic detection model.",
            "d) The data scientist creates the text prediction and builds one topic detection and two entity extraction models.",
            "e) The data scientist trains the text prediction: One topic detection model and several entity extraction models."
        ],
        "answer": "a, b, e"
    },
    {
        "question": "You can use various data types in adaptive analytics. Some of these require preprocessing before being used as a potential predictor. Others can be used directly. Which two data types require no preprocessing? (Choose Two)",
        "options": [
            "a) Event stream data, such as recent transactions",
            "b) Symbolic data with up to 200 distinct values, such as products bought previously",
            "c) Text data such as Twitter messages",
            "d) Dates with absolute time/date values, such as birthdays",
            "e) Numeric data such as customer age and income"
        ],
        "answer": "d, e"
    },
    {
        "question": "The purpose of regular inspection is to detect factors that negatively influence the performance of the adaptive models and the success rate of the actions. Which two issues should be discussed with the business? (Choose Two)",
        "options": [
            "a) Actions that are offered so often that they dominate other actions",
            "b) Actions that have a low number of responses",
            "c) Actions for which the model is not predictive",
            "d) Predictors with a low performance",
            "e) Predictors that are never used"
        ],
        "answer": "a, d"
    },
    {
        "question": "What are two results of an Adaptive Model? (Choose Two)",
        "options": [
            "a) Priority",
            "b) Propensity",
            "c) Segment",
            "d) Performance"
        ],
        "answer": "c, d"
    },
    {
        "question": "As a Data Scientist you want to use a predictive model to detect potential churn for a telco company. Which three options do you have? (Choose Three)",
        "options": [
            "a) Create a Text extraction model",
            "b) Use a Google ML model",
            "c) Use Pega machine learning to build a model",
            "d) Import a third-party PMML model",
            "e) Create an adaptive self-learning model"
        ],
        "answer": "a, c, d"
    },
    {
        "question": "The objective of Pega Process AI™ is to interpret the incoming data and then decide on the best action to take. In which two ways can you better analyze the incoming data? (Choose Two)",
        "options": [
            "a) Event processing",
            "b) Predictive analytics",
            "c) Text analytics",
            "d) Decision strategies",
            "e) Business Rules"
        ],
        "answer": "a, c"
    },
    {
        "question": "Creating predictive models Using Prediction Studio to build Pega machine learning models on historical data, you can build two types of models: ____________ and ____________. (Choose Two)",
        "options": [
            "a) adaptive models",
            "b) continuous models",
            "c) binary models",
            "d) voice to text model"
        ],
        "answer": "b, c"
    },
    {
        "question": "U+ Air recently enabled a chatbot on its website to interact with customers. The airline asked a data scientist to configure the chatbot to recognize all ticket number patterns that the airline uses. The company wants the chatbot to be resistant to human error and detect also unusual ticket numbers. Which combination of entity extraction methods can the data scientist implement to achieve this business requirement? (Choose Two)",
        "options": [
            "a) Machine learning",
            "b) Keywords",
            "c) Ruta script",
            "d) Topic detection"
        ],
        "answer": "a, c"
    },
    {
        "question": "To confirm the continuing accuracy of your adaptive models, adaptive models must be regularly inspected. Which two tasks are part of a regular inspection? (Choose Two)",
        "options": [
            "a) Adjust the advanced settings.",
            "b) Check the performance of individual predictors.",
            "c) Check the performance and success rate of the models.",
            "d) Update the models.",
            "e) Add the historical data collected since the last inspection."
        ],
        "answer": "b, c"
    },
    {
        "question": "With the standardized model operations process (MLOps), you can replace a low-performing predictive model that drives a prediction with an updated model. When you approve the model, the system automatically generates a change request in _________.",
        "options": [
            "a) the development environment",
            "b) the production environment",
            "c) an external environment",
            "d) the business operations environment"
        ],
        "answer": "d"
    },
    {
        "question": "How can data be integrated from multiple sources in Adaptive Analytics?",
        "options": [
            "a) Using ETL (Extract, Transform, Load) tools",
            "b) Manually copying and pasting data into one central location",
            "c) Using spreadsheets to merge data",
            "d) Only using data from one source"
        ],
        "answer": "a"
    },
    {
        "question": "Which of the following statements about chatbots is true?",
        "options": [
            "a) The chatbot can detect only entities that follow a strict text pattern.",
            "b) A text prediction that aims to detect the topic and entities in the message drives the chatbot.",
            "c) After the digital messaging channel creation, the chatbot maps the entities to case properties and saves them in a case that CSRs can view in the Customer Service portal.",
            "d) The prediction needs to be created in the Prediction Studio by the data scientist to enable the chatbot."
        ],
        "answer": "b"
    },
    {
        "question": "You enable the capture of historical data in an adaptive model. Which two data elements does the system capture for every customer interaction? (Choose Two)",
        "options": [
            "a) The value of all predictors.",
            "b) The value of only the active predictors.",
            "c) The model metadata.",
            "d) The propensity the model generates.",
            "e) The outcome of the interaction."
        ],
        "answer": "a, e"
    },
    {
        "question": "When you build a model by using Pega machine learning, Pega machine learning uses the validation holdout set to ____________ and to ____________.",
        "options": [
            "a) select the best model",
            "b) compare the performance of candidate models",
            "c) check for robustness of candidate models",
            "d) train the models",
            "e) analyze the performance characteristics of candidate models"
        ],
        "answer": "b, c"
    },
    {
        "question": "What is the role of a compliance officer?",
        "options": [
            "a) To manage an organization's compliance with financial regulations",
            "b) To manage an organization's compliance with environmental regulations",
            "c) To manage an organization's compliance with legal and regulatory obligations",
            "d) To manage an organization's compliance with customer needs"
        ],
        "answer": "c"
    },
    {
        "question": "The implementation of Next-Best-Action must involve __________.",
        "options": [
            "a) inclusion of third party predictive models",
            "b) defining a prioritization formula using contact policies",
            "c) building a product catalog",
            "d) defining business issue and group hierarchy"
        ],
        "answer": "b"
    },
    {
        "question": "U+ Insurance uses Pega Process AI™ to optimize case management and applies adaptive models to predict the outcome of claim cases. In this scenario, the system creates an adaptive model for each _____________.",
        "options": [
            "a) Case type step",
            "b) Case type stage",
            "c) Case type",
            "d) Case"
        ],
        "answer": "b"
    },
    {
        "question": "What types of analyses occur at the high level of natural language processing (NLP)? (Choose Three)",
        "options": [
            "a) Casual analysis",
            "b) Syntactic analysis",
            "c) Linguistic analysis",
            "d) Exploratory analysis",
            "e) Semantic analysis",
            "f) Inferential analysis"
        ],
        "answer": "b, c, e"
    },
    {

        "question": "U+ Bank shows mortgage offers on its website by using Pega Customer Decision Hub™. As a data scientist at U+ Bank, you suspect that if the number of customer visits to the mortgages web page increases, the increase might mean a higher interest in the product. Currently, there is no such field in the customer data model. To verify your hypothesis, you create ____________.",
        "options": [
            "A. a parameterized predictor",
            "B. an Interaction History (IH) summary",
            "C. a strategy",
            "D. a non-parameterized predictor"
        ],
        "answer": "A"
    },
    {
        "question": "Which of the following is a Pega tool used for NLP?",
        "options": [
            "A. Pega Dialogue Manager",
            "B. Pega Decision Management",
            "C. Pega Knowledge Management",
            "D. Pega Text Analyzer"
        ],
        "answer": "D"
    },
    {
        "question": "Which component(s) do you use to calculate the average margin of four actions?",
        "options": [
            "A. four Set Property components",
            "B. one Group By component",
            "C. four Group By components",
            "D. one Set Property component"
        ],
        "answer": "D"
    },
    {
        "question": "When developing a predictive model, the outcome of a spectrum model can indicate the _______________.",
        "options": [
            "A. probability of a loan default",
            "B. probability of churn",
            "C. acceptance of an offer",
            "D. purchase value of a campaign respondent"
        ],
        "answer": "D"
    },
    {
        "question": "A Text Analyzer performs natural language processing on a piece of text. It then produces a structured output, which can be analyzed using reports. What type of text analysis does the text analyzer perform?",
        "options": [
            "A. Word analysis",
            "B. Word count",
            "C. Classification",
            "D. Cross reference analysis"
        ],
        "answer": "A"
    },
    {
        "question": "To enable an assessment of its reliability, the Adaptive Model produces three outputs: Propensity, Performance and Evidence. The performance of an Adaptive Model that has not collected any evidence is_________.",
        "options": [
            "A. 1-0",
            "B. 0.0",
            "C. 0.5",
            "D. null"
        ],
        "answer": "C"
    },
    {
        "question": "Which of the following is a key feature of Pega Process AI?",
        "options": [
            "A. Real-time analytics and insights",
            "B. Process automation and orchestration",
            "C. Predictive modeling and analysis",
            "D. All of the above"
        ],
        "answer": "D"
    },
    {
        "question": "A strategy designer has created 10 actions in the Sales/Credit Cards group and 10 actions in the Sales/Mortgages group. He would like to import all 10 actions from the Credit Cards group and only two actions from the Mortgage group into one decision strategy. What is the minimum number of Proposition Data components he needs to use in his strategy?",
        "options": [
            "A. one",
            "B. two",
            "C. twelve",
            "D. three"
        ],
        "answer": "D"
    },
    {
        "question": "Model transparency is becoming an important requirement for many businesses. In Prediction Studio, model transparency thresholds can be set for ________________.",
        "options": [
            "A. a business issue",
            "B. a model type",
            "C. a model",
            "D. a department"
        ],
        "answer": "A"
    },
    {
        "question": "Pega Customer Decision Hub™ uses the P*C*V*L arbitration formula to select the next best action for each customer. Which factor in the arbitration formula is calculated by using AI?",
        "options": [
            "A. Context weighing",
            "B. Business levers",
            "C. Propensity",
            "D. Value"
        ],
        "answer": "C"
    },
    {
        "question": "In a strategy defined in the 'Retention' issue and the 'X-Sell' group, you can import __________.",
        "options": [
            "A. propositions from the Sales issue",
            "B. propositions from all groups under the 'Retention' issue",
            "C. all propositions from the system",
            "D. propositions from 'X-Sell' group"
        ],
        "answer": "A"
    },
    {
        "question": "A data scientist creates a predictive model to predict the likelihood of a customer leaving the bank in the near future. The predictive model aggregates the classes into three classification groups: high churn risk, medium churn risk, and low churn risk. As a decisioning consultant, you need to reference the result of this classification in a decision strategy. Which property allows you to do so?",
        "options": [
            "A. pyOutcome",
            "B. PropertyHasValue",
            "C. pyPropensity",
            "D. pxSegment"
        ],
        "answer": "D"
    },
    {
        "question": "The Filter component is used to filter ________________.",
        "options": [
            "A. adaptive models",
            "B. attributes",
            "C. action",
            "D. customers"
        ],
        "answer": "A"
    },
    {
        "question": "The goal of entity extraction is to interpret the incoming data and detect the necessary entity. Which two methods can you use to achieve this business outcome? (Choose Two)",
        "options": [
            "A. Ruta script",
            "B. Topic detection",
            "C. Machine learning",
            "D. Keywords"
        ],
        "answer": ["A", "C"]
    },
    {
        "question": "To optimize their customer interactions, U+ Bank routes all emails that are complaints to a specialized department. To identify emails that voice a complaint, the text prediction uses ___________.",
        "options": [
            "A. a sentiment model",
            "B. a language model",
            "C. a topic model",
            "D. an entity extraction model"
        ],
        "answer": "C"
    },
    {
        "question": "What are some common challenges in applying machine learning in Adaptive Analytics?",
        "options": [
            "A. Limited availability of labeled data",
            "B. Difficulty in selecting the right algorithms",
            "C. Lack of skilled resources",
            "D. All of the above"
        ],
        "answer": "D"
    },
    {
        "question": "Predictions combine predictive analytics and best practices in data science. As a data scientist, what is a valid reason to adjust the default response timeout in a prediction?",
        "options": [
            "A. Increase lift",
            "B. Optimize the success rate",
            "C. Limit the number of responses",
            "D. Suit the use case"
        ],
        "answer": "D"
    },
    {
        "question": "Which of these belong to the same group as the Prioritize component?",
        "options": [
            "A. Proposition",
            "B. Data Join",
            "C. Arbitration",
            "D. Filter"
        ],
        "answer": "D"
    },
    {
        "question": "Adaptive model components can output ____________.",
        "options": [
            "A. an optimised strategy",
            "B. a proposition",
            "C. the number of customers eligible for a proposition",
            "D. the customer's propensity to accept a proposition"
        ],
        "answer": "D"
    },
    {
        "question": "Using Prediction Studio to build Pega machine learning modeltion formula to select the next best action for each customer. \n Which factor in the arbitration formula does AI calculate?",
        "options": [
            "a) Context weighing",
            "b) Business levers",
            "c) Action value",
            "d) Propensity"
        ],
        "answer": "d"
    },
    {
        "question": "What is time series analysis?",
        "options": [
            "a) A statistical technique for analyzing cross-sectional data",
            "b) A statistical technique for analyzing longitudinal data",
            "c) A statistical technique for analyzing time-dependent data",
            "d) A statistical technique for analyzing categorical data"
        ],
        "answer": "c"
    },
    {
        "question": "As a data scientist, you are tasked with creating a new prediction that estimates the likelihood that a claim is fraudulous. The application developer wants to proceed and use the prediction in a case type to test the application. \n To unblock the application developer, which task do you prioritize?",
        "options": [
            "a) Create the predictive model that drives the prediction",
            "b) Create the customer data model",
            "c) Create a placeholder scorecard to drive the prediction",
            "d) Create the prediction"
        ],
        "answer": "d"
    },
    {
        "question": "When predictors have a similar predicting performance, they are automatically grouped. \n What happens when predictors are grouped?",
        "options": [
            "a) The predictors are merged into one.",
            "b) One predictor is used by the model; the others are deactivated.",
            "c) One predictor is used by the model, the others are deleted.",
            "d) All predictors are used by the model."
        ],
        "answer": "b"
    },
    {
        "question": "The U+ Insurance wants straight-through processing of claims with a low fraud risk. As a data scientist, you create a prediction that calculates the probability that a claim is fraudulent. \n What type of prediction do you create?",
        "options": [
            "a) Text analytics",
            "b) Customer Decision Hub",
            "c) Case management",
            "d) Strategic"
        ],
        "answer": "c"
    },
    {
        "question": "A coffee company wants to simulate decisions that requires large amounts of data. However, the organization's live data is inaccessible. The Monte Carlo method _____.",
        "options": [
            "a) makes the organisation's live data accessible",
            "b) generates data that the company can use as input for adaptive decisioning",
            "c) generates millions of rows with minimal effort",
            "d) combines external data sets into a larger data set"
        ],
        "answer": "c"
    },
    {
        "question": "The process of importing a third-party predictive model into Pega is_____________?",
        "options": [
            "a) to first convert it into the Pega markup language",
            "b) similar to importing an adaptive model",
            "c) the same as importing a Pega predictive model",
            "d) simpler than importing a Pega predictive model"
        ],
        "answer": "a"
    },
    {
        "question": "The Prediction Studio portal supports the creation of two distinct types of predictive Scoring models are used to__________________.",
        "options": [
            "a) score different propositions",
            "b) predict binary behavior",
            "c) predict continuous behavior",
            "d) differentiate between good, better and best"
        ],
        "answer": "b"
    },
    {
        "question": "U+ Telecom wants to engage in proactive retention to reduce churn. As a data scientist, you create a prediction that calculates the probability that a client is likely to cancel a subscription. \n What type of prediction do you create?",
        "options": [
            "a) Customer Decision Hub",
            "b) Text analytics",
            "c) Case management",
            "d) Strategic"
        ],
        "answer": "a"
    },
    {
        "question": "The goal of Pega Process AI is to interpret the incoming data and then decide on the best action to take. \n In which two ways can you better analyze the incoming data?",
        "options": [
            "a) Event processing",
            "b) Text analytics",
            "c) Predictive analytics",
            "d) Business rules",
            "e) Decision strategies"
        ],
        "answer": "a"
    },
    {
        "question": "The use of an imported third-party model in a decision strategy is____",
        "options": [
            "a) Only possible after conversion into a Pega machine learning model",
            "b) Only possible after conversion into Pega markup language",
            "c) Identical to the use of an adaptive model",
            "d) Similar to the use of a model built with Pega machine learning"
        ],
        "answer": "d"
    },
    {
        "question": "Which of the following is a technique used in Pega Process AI for predicting process outcomes?",
        "options": [
            "a) Decision trees",
            "b) K-Means clustering",
            "c) Linear regression",
            "d) Neural networks"
        ],
        "answer": "d"
    },
    {
        "question": "In a decision strategy, to import actions you use a(n) _____________________.",
        "options": [
            "a) Offer data component",
            "b) Data import component",
            "c) Proposition data component",
            "d) Import data component"
        ],
        "answer": "b"
    },
    {
        "question": "In a decision strategy, what does a dotted line from a Group By component to a Filter component indicate?",
        "options": [
            "a) Information from the Group By component is copied over to the Filter component.",
            "b) There is a one-to-one relationship between the Group By and the Filter components.",
            "c) The Filter component references a property from Group By component.",
            "d) Evaluate the Filter component first to evaluate the Group By component."
        ],
        "answer": "c"
    },
    {
        "question": "A telecommunications company wants to apply text analysis to incoming emails to understand how satisfied its customers are about various products and services. That requires processing of the natural language of the email texts. \n Which analysis occurs during natural language processing?",
        "options": [
            "a) Intent analysis",
            "b) Presumptive analysis",
            "c) Subjective analysis",
            "d) Semantic analysis"
        ],
        "answer": "d"
    },
    {
        "question": "Model transparency is an important requirement for many businesses. In Prediction Studio, you set model transparency thresholds for ________________. ",
        "options": [
            "a) a model type",
            "b) a model",
            "c) a business issue",
            "d) a department"
        ],
        "answer": "c"
    },
    {
        "question": "Adaptive model strategy components can output ____________. ",
        "options": [
            "a) the number of customers eligible for an action",
            "b) an optimized strategy",
            "c) the customer's propensity to accept an action",
            "d) an action"
        ],
        "answer": "c"
    },
    {
        "question": "Many companies already use third-part predictive models and want to reuse these assets in the Pega Decision Management landscape. Which decision component allows you to use a third-party Credit Risk Model 80% of the time and a Pega Credit Risk Model 20%? ",
        "options": [
            "a) Switch",
            "b) Adaptive Model",
            "c) Filter",
            "d) Champion Challenger"
        ],
        "answer": "a"
    },
    {
        "question": "What is reinforcement learning in Adaptive Analytics? ",
        "options": [
            "a) A machine learning technique that involves training a model on a large amount of data",
            "b) A technique for improving the accuracy of existing machine learning models",
            "c) A technique for learning from feedback and adjusting decision-making processes in real-time",
            "d) A technique for detecting anomalies in data"
        ],
        "answer": "c"
    },
    {
        "question": "When during a customer interaction should a Next-Best-Action decision be made? ",
        "options": [
            "a) Every time new information is received",
            "b) When the customer intent is captured",
            "c) First time the customer is shown a banner",
            "d) At the beginning of customer call"
        ],
        "answer": "a"
    },
    {
        "question": "Using Prediction Studio to build Pega machine learning models on historical data, you can build two types of models: ____________ and ____________. (Choose Two) ",
        "options": [
            "a) continuous models",
            "b) voice to text model",
            "c) binary models",
            "d) adaptive models"
        ],
        "answer": ["a", "c"]
    },
    {
        "question": "Which Predictive Modeling Markup Language (PMML) model type is supported by Pega? ",
        "options": [
            "a) Regression Model",
            "b) Adaptive model",
            "c) Text Model",
            "d) Decision Table"
        ],
        "answer": "a"
    },
    {
        "question": "What is feature engineering in Predictive Analytics? ",
        "options": [
            "a) The process of selecting which data to use in a model",
            "b) The process of transforming raw data into features that can be used in a model",
            "c) The process of testing and validating a model",
            "d) The process of deploying a model in a production environment"
        ],
        "answer": "b"
    },
    {
        "question": "What is the difference between hierarchical and k-means clustering? ",
        "options": [
            "a) Hierarchical clustering is a supervised learning technique, while k-means clustering is an unsupervised learning technique",
            "b) Hierarchical clustering is a clustering technique that produces a dendrogram, while k-means clustering is a flat clustering technique",
            "c) Hierarchical clustering is a flat clustering technique, while k-means clustering is a clustering technique that produces a dendrogram",
            "d) Hierarchical clustering and k-means clustering are the same thing"
        ],
        "answer": "b"
    },
    {
        "question": "U+ Insurance wants to predict successful completion of car insurance claims but has no historical data. Which rule type do you use in this scenario? ",
        "options": [
            "a) Adaptive model",
            "b) PMML model",
            "c) Decision table",
            "d) When rule"
        ],
        "answer": "a"
    },
    {
        "question": "Who is responsible for adding precalculated model scores to the Customer Decision Hub data model? ",
        "options": [
            "a) The Data Scientist",
            "b) The technical team",
            "c) The Revision Manager",
            "d) The Team Lead"
        ],
        "answer": "b"
    },
    {
        "question": "What is the difference between supervised and unsupervised learning in Adaptive Analytics? ",
        "options": [
            "a) Supervised learning requires labeled data, while unsupervised learning does not",
            "b) Unsupervised learning requires labeled data, while supervised learning does not",
            "c) Both supervised and unsupervised learning require labeled data",
            "d) Neither supervised nor unsupervised learning require labeled data"
        ],
        "answer": "a"
    },
    {
        "question": "The purpose of model templates in Pega machine learning is ____________. ",
        "options": [
            "a) to set the model outcomes",
            "b) to streamline model deployment",
            "c) to set the model context",
            "d) to streamline model development"
        ],
        "answer": "d"
    },
    {
        "question": "What are the benefits of using Adaptive Analytics? ",
        "options": [
            "a) Faster insights from data",
            "b) More accurate predictions",
            "c) Increased agility in responding to changing business needs",
            "d) Improved customer service"
        ],
        "answer": "c"
    }
]


class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Scientist Quiz")
        self.master.geometry("700x400")

        self.score = 0
        self.current_question = 0

# Show the welcome message
        self.welcome_label = tk.Label(self.master, text="Welcome to the Data Scientist Quiz!\nAnswer the questions by selecting the correct option.\nLet's begin!", font=("Arial", 16), justify="center")
        self.welcome_label.pack(pady=50)

        # Start button to begin quiz
        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz, font=("Arial", 12))
        self.start_button.pack(pady=20)

    def start_quiz(self):
        self.welcome_label.destroy()  # Remove the welcome message
        self.start_button.destroy()  # Remove the start button

        # Frame for the question
        self.question_frame = tk.Frame(self.master)
        self.question_frame.pack(pady=20)

        self.question_label = tk.Label(self.question_frame, text="", wraplength=650, font=("Arial", 14))
        self.question_label.pack()

        # Frame for the options
        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack(pady=10)

        self.var = tk.StringVar()

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.var, value="", font=("Arial", 12))
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        # Frame for feedback display
        self.feedback_label = tk.Label(self.master, text="", font=("Arial", 14), fg="green")
        self.feedback_label.pack(pady=20)

        # Button to show feedback
        self.feedback_button = tk.Button(self.master, text="Show Feedback", command=self.show_feedback, font=("Arial", 12))
        self.feedback_button.pack(pady=10)

        # Button to go to next question
        self.next_button = tk.Button(self.master, text="Next Question", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
            self.var.set(None)
            for idx, option in enumerate(q['options']):
                self.radio_buttons[idx].config(text=option, value=option[0].lower())
        else:
            self.show_score()

    def show_feedback(self):
        selected = self.var.get()
        if not selected:
            self.feedback_label.config(text="Please select an option before proceeding.", fg="red")
            return
        correct_answer = questions[self.current_question]['answer']
        if selected == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            correct_option = next(opt for opt in questions[self.current_question]['options'] if opt.startswith(correct_answer))
            self.feedback_label.config(text=f"Wrong! The correct answer is: {correct_option}", fg="red")

    def next_question(self):
        # Clear feedback before going to the next question
        self.feedback_label.config(text="", fg="green")

        selected = self.var.get()

        correct_answer = questions[self.current_question]['answer']
        if selected == correct_answer:
            self.score += 1

        self.current_question += 1
        self.load_question()

    def show_score(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        score_percentage = (self.score / len(questions)) * 100
        score_text = f"You scored {self.score} out of {len(questions)} ({score_percentage}%)"
        score_label = tk.Label(self.master, text=score_text, font=("Arial", 16))
        score_label.pack(pady=50)

        if self.score == len(questions):
            feedback = "Excellent! You have a strong grasp of the material."
        elif self.score >= len(questions) // 2:
            feedback = "Good job! You might want to review a few concepts."
        else:
            feedback = "Keep studying! Revisit the material for better understanding."

        feedback_label = tk.Label(self.master, text=feedback, font=("Arial", 14))
        feedback_label.pack()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()