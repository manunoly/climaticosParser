/**
 * Created by manuel on 28/07/15.
 */



   $(document).ready(function() {
    $(function () {
       var options = {
            chart: {
                renderTo: 'temperatura',
                type: 'line',
                marginRight: 30,
                marginBottom: 25
            },
            title: {
                text: 'Grafica de Temperatura',
                x: -20 //center
            },
           rangeSelector: {
                        selected: 4
                    },
            subtitle: {
                text: '',
                x: -20
            },
           /*
{#               xAxis: {#}
{#                    type: 'datetime',#}
{#                    labels: {#}
{#                        format: '{%Y-%b-%e}',#}
{#                        align: 'right',#}
{#                        rotation: -30#}
{#                    }#}
{#                },#}
{#                   xAxis: {#}
{#            type: 'datetime',#}
{#            labels: {#}
{#                format: '{value:%Y-%m-%d}',#}
{#                rotation: 45,#}
{#                align: 'left'#}
{#            }#}
{#        },#}*/
            xAxis:[{
              labels:{
                 formatter:function(){
                     return Highcharts.dateFormat('%Y-%m-%d',this.value);
                 }
              }
            }],
            yAxis: {
                title: {
                    text: 'Temperatura'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
           tooltip: {
                        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
                        valueDecimals: 2
                    },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: []
        }

        $.getJSON("temperaturaJson", function(json) {
            options.xAxis.categories = json[0]['data'];
            options.series[0] = json[1];
            options.series[1] = json[2];
            options.series[2] = json[3];
            chart = new Highcharts.StockChart(options);
        });
    });

//{#Grafica de Humedad Relativa#}
    $(function () {
       var options = {
            chart: {
                renderTo: 'humedad',
                type: 'line',
                marginRight: 30,
                marginBottom: 25
            },
            title: {
                text: 'Grafica de Humedad Relativa',
                x: -20 //center
            },
           rangeSelector: {
                        selected: 4
                    },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis:[{
              labels:{
                 formatter:function(){
                     return Highcharts.dateFormat('%Y-%m-%d',this.value);
                 }
              }
            }],
            yAxis: {
                title: {
                    text: 'Humedad Realativa'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
           tooltip: {
                        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
                        valueDecimals: 2
                    },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: []
        }

        $.getJSON("humedadJson", function(json) {
            options.xAxis.categories = json[0]['data'];
            options.series[0] = json[1];
            options.series[1] = json[2];
            options.series[2] = json[3];
            chart = new Highcharts.StockChart(options);
        });
    });

//{#  presionBarometrica#}
     $(function () {
       var options = {
            chart: {
                renderTo: 'presionBarometrica',
                type: 'line',
                marginRight: 30,
                marginBottom: 25
            },
            title: {
                text: 'Grafica de Presion Barometrica',
                x: -20 //center
            },
           rangeSelector: {
                        selected: 4
                    },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis:[{
              labels:{
                 formatter:function(){
                     return Highcharts.dateFormat('%Y-%m-%d',this.value);
                 }
              }
            }],
            yAxis: {
                title: {
                    text: 'Presion Barometrica'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
           tooltip: {
                        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
                        valueDecimals: 2
                    },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: []
        }

        $.getJSON("presionBarometricaJson", function(json) {
            options.xAxis.categories = json[0]['data'];
            options.series[0] = json[1];
            options.series[1] = json[2];
            options.series[2] = json[3];
            chart = new Highcharts.StockChart(options);
        });
    });

//{#  Viento#}
     $(function () {
       var options = {
            chart: {
                renderTo: 'viento',
                type: 'line',
                marginRight: 30,
                marginBottom: 25
            },
            title: {
                text: 'Grafica de Velocidad del Viento',
                x: -20 //center
            },
           rangeSelector: {
                        selected: 4
                    },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis:[{
              labels:{
                 formatter:function(){
                     return Highcharts.dateFormat('%Y-%m-%d',this.value);
                 }
              }
            }],
            yAxis: {
                title: {
                    text: 'Velocidad del Viento'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
           tooltip: {
                        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
                        valueDecimals: 2
                    },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: []
        }

        $.getJSON("vientoJson", function(json) {
            options.xAxis.categories = json[0]['data'];
            options.series[0] = json[1];
            options.series[1] = json[2];
            options.series[2] = json[3];
            chart = new Highcharts.StockChart(options);
        });
    });

/*
{#        $(function () {#}
{#            var seriesOptions = [],#}
{#                seriesCounter = 0,#}
{#                names = ['TAP', 'TAMax', 'TAMin'],#}
{#                // create the chart when all data is loaded#}
{#                createChart = function () {#}
{##}
{#                    $('#containerGraf').highcharts('StockChart', {#}
{##}
{#                        rangeSelector: {#}
{#                            selected: 4#}
{#                        },#}
{##}
{#                        yAxis: {#}
{#                            labels: {#}
{#                                formatter: function () {#}
{#                                    return (this.value > 0 ? ' + ' : '') + this.value + '%';#}
{#                                }#}
{#                            },#}
{#                            plotLines: [{#}
{#                                value: 0,#}
{#                                width: 2,#}
{#                                color: 'silver'#}
{#                            }]#}
{#                        },#}
{##}
{#                        plotOptions: {#}
{#                            series: {#}
{#                                compare: 'percent'#}
{#                            }#}
{#                        },#}
{##}
{#                        tooltip: {#}
{#                            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',#}
{#                            valueDecimals: 2#}
{#                        },#}
{##}
{#                        series: seriesOptions#}
{#                    });#}
{#                };#}
{##}
{#            $.each(names, function (i, name) {#}
{##}
{#                $.getJSON('temperaturaJson/' + name.toLowerCase(),    function (data) {#}
{##}
{#                    seriesOptions[i] = {#}
{#                        name: name,#}
{#                        data: data#}
{#                    };#}
{##}
{#                    // As we're loading the data asynchronously, we don't know what order it will arrive. So#}
{#                    // we keep a counter and create the chart when all the data is loaded.#}
{#                    seriesCounter += 1;#}
{##}
{#                    if (seriesCounter === names.length) {#}
{#                        createChart();#}
{#                    }#}
{#                });#}
{#            });#}
{#        });#}*/
         $("#buscarbd").click( function()
           {
             alert('button clicked');
           }
        );
        $('#example').dataTable( {

            "dom": '<"top"Cfl>rt<"bottom"ip><"clear">',
                "colVis": {
                    "buttonText": "Mostrar/Ocultar Columnas",
                    restore: "Reiniciar",
                    showAll: "Mostrar Todos",
                    showNone: "Mostrar Ninguno"
                },
            "ajax": {
                "url": "cargarDatos",
                data: 'data'
            },
            "aoColumns": [
//{#                    { "mData": "Estacion" },#}
                { "mData": "fecha" },
                { "mData": "temperaturaAirePromedio" },
                { "mData": "temperaturaAireMaxima" },
                { "mData": "temperaturaAireMinima" },
                { "mData": "humedadRelativaPromedio" },
                { "mData": "humedadRelativaMaxima" },
                { "mData": "humedadRelativaMinima" },
                { "mData": "presionBarometricaPromedio" },
                { "mData": "presionBarometricaMaxima" },
                { "mData": "presionBarometricaMinima" },
                {"bVisible": false, "mData": "radiacionSolarGlobalPromedio" },
                {"bVisible": false, "mData": "radiacionSolarGlobalMaxima" },
                {"bVisible": false, "mData": "radiacionSolarGlobalMinima" },
                {"bVisible": false, "mData": "radiacionSolarGlobalSumatoria" },
                {"bVisible": false, "mData": "radiacionSolarDifusaPromedio" },
                {"bVisible": false, "mData": "radiacionSolarDifusaMaxima" },
                {"bVisible": false, "mData": "radiacionSolarDifusaMinima" },
                {"bVisible": false, "mData": "radiacionSolarDifusaSumatoria" },
                { "mData": "vientoDireccionPromedio" },
                { "mData": "vientoDireccionMaxima" },
                {"bVisible": false, "mData": "vientoDireccionRachaMaxima" },
                {"bVisible": false, "mData": "vientoHoraRacha" },
                {"bVisible": false, "mData": "vientoMinutoRacha" },
                { "mData": "vientoVelocidadPromedio" },
                { "mData": "vientoVelocidadMaxima" },
                { "mData": "vientoVelocidadMinima" },
                {"bVisible": false, "mData": "vientoRecorrido" },
                {"bVisible": false, "mData": "voltajeBateria" }
            ]

        } );
    } );
