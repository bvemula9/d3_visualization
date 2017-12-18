
Summary:
	I have chosen weekly US petroleum data from CFTC and ICE websites. I have developed xls_to_csv.py python code to run the code on Friday 14:40 and Monday 6:40 to obtain data from CFTC and ICE websites respectively. I have cleaned the data and added a new column named spot price from a different source. I have finally generated CSV files. The csv files are used to plot visualization graphs. I graphs I have generated are multi-line graphs. I have generated two multi-line charts, first multi- line chart shows comparison of various net values and the second multi-line chart shows the comparison of ratios and spot price. Legend is created and also mouse tooltip is created to indicate values when mover is moved over the line.


Instructions to run:

When the index.html code is running, you will see two dropdowns at the bottom of the page. First dropdown is for selecting the csv files from the three final csv’s created. The second dropdown is for filtering the particular row from the selected csv. When they both are selected, then you will see the two multi-line graphs, one comparing the net values and other comparing ratios. The second graph is having dual y-axis, one for ratios and other for spot_price. This is because the range of values are different. 

Important Notes:
Please disable the cross origin request in the browser to run the code.


Design:
Initially, I have created multiple graphs for all the csv’s individually for all the rows. Then I was suggested to use filtering process to select the csv and row externally. So I have created a dropdown feature to allow filtering option to the user. Then, I was suggested to include spot price also along with the ratios, for which I have created dual y-axis multi-line chart. Finally, when the graphs are ready and plotted, it was hard to identify the values just by looking at the lines. So I have used tooltip feature to indicate the values when the mouse is placed at that point on the line.

Feedbacks:
•	Person 1: Alex Vugman
    Feedback: Add Filtering and give option to the user to make it more user friendly.
•	Person 2: Cagri
    Feedback: Add spot_price along with the ratios.
•	Person 3: Nitish Reddy
    Feedback: Show the values when move hovered over the lines to make user understand the amount of rise or fall in 
              the values.

Outcomes:
•   The net value of prod i.e., Prod_net value has increased drastically from mid july for CFTC futures in Europe  
    whereas in New York, it remained constant.
•   The Swap_net value in CFTC Futures and Options has decreased from august 2017 in Europe whereas in increased in 
    New York area.
    
Resources and References:
•	https://classroom.udacity.com/nanodegrees
•	https://stackoverflow.com/
•	https://bl.ocks.org/mbostock/3884955

