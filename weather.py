{
    "@context": [
        "https://geojson.org/geojson-ld/geojson-context.jsonld",
        {
            "@version": "1.1",
            "wx": "https://api.weather.gov/ontology#",
            "s": "https://schema.org/",
            "geo": "http://www.opengis.net/ont/geosparql#",
            "unit": "http://codes.wmo.int/common/unit/",
            "@vocab": "https://api.weather.gov/ontology#",
            "geometry": {
                "@id": "s:GeoCoordinates",
                "@type": "geo:wktLiteral"
            },
            "city": "s:addressLocality",
            "state": "s:addressRegion",
            "distance": {
                "@id": "s:Distance",
                "@type": "s:QuantitativeValue"
            },
            "bearing": {
                "@type": "s:QuantitativeValue"
            },
            "value": {
                "@id": "s:value"
            },
            "unitCode": {
                "@id": "s:unitCode",
                "@type": "@id"
            },
            "forecastOffice": {
                "@type": "@id"
            },
            "forecastGridData": {
                "@type": "@id"
            },
            "publicZone": {
                "@type": "@id"
            },
            "county": {
                "@type": "@id"
            }
        }
    ],
    "id": "https://api.weather.gov/stations/KCLS/observations/2024-11-22T15:55:00+00:00",
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [
            -122.98,
            46.68
        ]
    },
    "properties": {
        "@id": "https://api.weather.gov/stations/KCLS/observations/2024-11-22T15:55:00+00:00",
        "@type": "wx:ObservationStation",
        "elevation": {
            "unitCode": "wmoUnit:m",
            "value": 54
        },
        "station": "https://api.weather.gov/stations/KCLS",
        "timestamp": "2024-11-22T15:55:00+00:00",
        "rawMessage": "KCLS 221555Z AUTO 00000KT 5SM -DZ FEW006 BKN012 OVC070 07/07 A2954 RMK AO2",
        "textDescription": "Light Drizzle",
        "icon": "https://api.weather.gov/icons/land/day/rain?size=medium",
        "presentWeather": [
            {
                "intensity": "light",
                "modifier": null,
                "weather": "drizzle",
                "rawString": "-DZ"
            }
        ],
        "temperature": {
            "unitCode": "wmoUnit:degC",
            "value": 7,
            "qualityControl": "V"
        },
        "dewpoint": {
            "unitCode": "wmoUnit:degC",
            "value": 7,
            "qualityControl": "V"
        },
        "windDirection": {
            "unitCode": "wmoUnit:degree_(angle)",
            "value": 0,
            "qualityControl": "V"
        },
        "windSpeed": {
            "unitCode": "wmoUnit:km_h-1",
            "value": 0,
            "qualityControl": "V"
        },
        "windGust": {
            "unitCode": "wmoUnit:km_h-1",
            "value": null,
            "qualityControl": "Z"
        },
        "barometricPressure": {
            "unitCode": "wmoUnit:Pa",
            "value": 100030,
            "qualityControl": "V"
        },
        "seaLevelPressure": {
            "unitCode": "wmoUnit:Pa",
            "value": null,
            "qualityControl": "Z"
        },
        "visibility": {
            "unitCode": "wmoUnit:m",
            "value": 8050,
            "qualityControl": "C"
        },
        "maxTemperatureLast24Hours": {
            "unitCode": "wmoUnit:degC",
            "value": null
        },
        "minTemperatureLast24Hours": {
            "unitCode": "wmoUnit:degC",
            "value": null
        },
        "precipitationLastHour": {
            "unitCode": "wmoUnit:mm",
            "value": null,
            "qualityControl": "Z"
        },
        "precipitationLast3Hours": {
            "unitCode": "wmoUnit:mm",
            "value": null,
            "qualityControl": "Z"
        },
        "precipitationLast6Hours": {
            "unitCode": "wmoUnit:mm",
            "value": null,
            "qualityControl": "Z"
        },
        "relativeHumidity": {
            "unitCode": "wmoUnit:percent",
            "value": 100,
            "qualityControl": "V"
        },
        "windChill": {
            "unitCode": "wmoUnit:degC",
            "value": null,
            "qualityControl": "V"
        },
        "heatIndex": {
            "unitCode": "wmoUnit:degC",
            "value": null,
            "qualityControl": "V"
        },
        "cloudLayers": [
            {
                "base": {
                    "unitCode": "wmoUnit:m",
                    "value": 180
                },
                "amount": "FEW"
            },
            {
                "base": {
                    "unitCode": "wmoUnit:m",
                    "value": 370
                },
                "amount": "BKN"
            },
            {
                "base": {
                    "unitCode": "wmoUnit:m",
                    "value": 2130
                },
                "amount": "OVC"
            }
        ]
    }
}
