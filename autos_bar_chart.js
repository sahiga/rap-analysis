// Load the Visualization API and the piechart package.
google.load('visualization', '1.0', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.setOnLoadCallback(drawChart);

// Callback that creates and popliates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Brand');
    data.addColumn('number', 'Number of Songs');
    data.addRows(
	[['Mercedes-Benz', 93], ['Jeep', 34], ['Cadillac', 25], ['Chevrolet (Chevy)', 24], ['Lexus', 22], ['Rolls-Royce', 22], ['Bentley', 20], ['Tommy Kaira', 15], ['ASL', 15], ['Welch-Detroit', 13], ['BMW (Bimmer, Beemer, Beamer)', 12], ['Chalmers-Detroit', 12], ['Dodge', 8], ['Imperial', 8], ['Eagle', 8], ['Lincoln', 7], ['Jaguar', 7], ['Audi', 6], ['Nova', 6], ['Honda', 5], ['Hummer', 5], ['Maxwell', 4], ['Continental', 3], ['Acura', 3], ['Nissan', 3], ['Lotus', 3], ['Aston Martin', 2], ['Mazda', 2], ['Porsche', 2], ['Ford', 2], ['Buick', 2], ['Lea-Francis', 1], ['Maybach', 1], ['Saturn', 1], ['Cony', 1], ['Toyota', 1], ['Yamaha', 1], ['McLaren', 1], ['Plymouth', 1], ['Suzuki', 1], ['Mitsubishi', 1], ['Viking', 1], ['Welch', 1], ['TGE', 1]]);

    // Set chart options
    var options = {	'title':'Car Brands Mentioned in Hip-Hop Music',
                       	'width':840,
                       	'height':600,
			'colors':['#c40a32'],
			'fontSize':12,
			'fontName':'Helvetica',
			titleTextStyle: {
			    fontSize: 22
			},
			hAxis: {
			    title: 'Car Brands',
			    showTextEvery: 1,
			    slantedText: true,
			    slantedTextAngle: 90
			},
			vAxis: {
			    title: 'Number of Songs'
			},
			legend: {
			    position: 'none'
			}
		  };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}
