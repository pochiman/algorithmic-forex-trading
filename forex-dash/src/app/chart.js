import Plotly from 'plotly.js-dist';

export function drawChart(chartData, p, g, divName) {

    let trace = {
        x: chartData.time,
        close: chartData.mid_c,
        high: chartData.mid_h,
        low: chartData.mid_l,
        open: chartData.mid_o,
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
    }

    let data = [trace];

    let layout = {
        title: `Data for ${p} ${g}`,
        height: '100%',
        autosize: true
    };

    Plotly.newPlot(divName, data, layout, { responsive: true });
    Plotly.Plots.resize(document.getElementById(divName));
}
