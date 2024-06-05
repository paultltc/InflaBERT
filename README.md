# Enhancing Inflation Nowcasting with LLM - *Sentiment Analysis on News*
> *Does incorporating a news sentiment index improve inflation nowcasting, particularly during periods of high volatility such as the COVID-19 pandemic?*

Code repository for the `FIN-407` course project. The report is available at [https://github.com/paultltc/InflaBERT/report.pdf](https://github.com/paultltc/InflaBERT/report.pdf).

#### Abstract
*Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida mauris. Nam arcu libero, nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque. Pellentesque habitant morbi tristi que senectus et netus etmalesuada fames ac turpis egestas. Mauris ut leo. Cras viverra metus rhoncus sem. Nulla et lectus vestibulum urna fringilla ultrices. Phasellus eu tellus sit amet tortor gravida placerat. Integer sapien est, iaculis in, pretium quis, viverra ac, nunc. Praesent eget sem vel leo ultrices bibendum. Aenean faucibus. Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac, nulla. Curabitur auctor semper nulla. Donec varius orci eget risus. Duis nibh mi, congue eu, accumsan eleifend, sagittis quis, diam. Duis eget orci sit amet orci dignissim rutrum.*

#### Repository Description

- `eda.ipynb`: EDA Notebook. 
- `SA.ipynb`: ???
- `news.ipynb`: Notebook used to construct the `NEWS` index. Note that this notebook is designed to be run on **Google Colab**.
- `nowcaster.ipynb`: Notebook used to derive results of the section *Inflation Nowcaster*.


#### Code Requirements

- **ALFRED**: This code repository uses the [ALFRED Database](https://alfred.stlouisfed.org/). To have access to it, you will need an API key.
- **Python Libraries**: Install all packages required by running the following command:
    ```
    pip install -r requirements.txt
    ``` 