# Enhancing Inflation Nowcasting with LLM - *Sentiment Analysis on News*
> *Does incorporating a news sentiment index improve inflation nowcasting, particularly during periods of high volatility such as the COVID-19 pandemic?*

Code repository for the `FIN-407` course project. The report is available at [https://github.com/paultltc/InflaBERT/report.pdf](https://github.com/paultltc/InflaBERT/report.pdf).

#### Abstract
*This study explores integrating large language models (LLMs) into classic inflation nowcasting frameworks, particularly in light of high inflation volatility periods such as the COVID-19 pandemic. We propose \texttt{InflaBERT}, a BERT-based LLM fine-tuned to predict inflation-related sentiment in news. We use this model to produce \texttt{NEWS}, an index capturing the monthly sentiment of the news regarding inflation. Incorporating our expectation index into the Cleveland Fed’s model, which is only based on macroeconomic autoregressive processes, shows a marginal improvement in nowcast accuracy during the pandemic. This highlights the potential of combining sentiment analysis with traditional economic indicators, suggesting further research to refine these methodologies for better real-time inflation monitoring.*

#### Repository Description

- `news_eda.ipynb`: EDA Notebook. 
- `inflabert.ipynb`: Notebook used to build the `InflaBERT` model.
- `news.ipynb`: Notebook used to construct the `NEWS` index. Note that this notebook is designed to be run on **Google Colab**.
- `nowcaster.ipynb`: Notebook used to derive results of the section *Inflation Nowcaster*.
- `plots.ipynb`: Notebook used to derived most of the plots of the report.


#### Code Requirements

- **ALFRED**: This code repository uses the [ALFRED Database](https://alfred.stlouisfed.org/). To have access to it, you will need an API key.
- **Python Libraries**: Install all packages required by running the following command:
    ```
    pip install -r requirements.txt
    ``` 