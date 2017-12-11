from flask import Flask, jsonify
from flask import request
from util import DateConverter
from util import ListStringConverter
from util import ListIntConverter

app = Flask(__name__)


app.url_map.converters['date'] = DateConverter
app.url_map.converters['listofstrings'] = ListStringConverter
app.url_map.converters['listofints'] = ListIntConverter

route = [
    {
        'title': u'MADRID-LISBONNE-GRECE',
        'price': u'250$'
    }
]

details = [
    {
        'title': u'MADRID-LISBONNE',
        'price': u'100$'
    },
    {
        'title': u'LISBONNE-GRECE',
        'price': u'100$'
    },
    {
        'title': u'GRECE-MADRID',
        'price': u'100$'
    }
]

airports = [
    {
        "airports_cityCode": "COPENHAGEN",
        "airports_coordinates_latitude": "55.6181",
        "airports_coordinates_longitude": "12.6561",
        "airports_countryCode": "dk",
        "airports_iataCode": "CPH",
        "airports_name": "Copenhagen",
        "airports_regionCode": "BORNHOLM"
    },
    {
        "airports_cityCode": "ROME",
        "airports_coordinates_latitude": "41.8045",
        "airports_coordinates_longitude": "12.2508",
        "airports_countryCode": "it",
        "airports_iataCode": "FCO",
        "airports_name": "Rome Fiumicino",
        "airports_regionCode": "LAZIO"
    },
    {
        "airports_cityCode": "NEWCASTLE",
        "airports_coordinates_latitude": "55.0375",
        "airports_coordinates_longitude": "-1.69167",
        "airports_countryCode": "gb",
        "airports_iataCode": "NCL",
        "airports_name": "Newcastle",
        "airports_regionCode": "TYNE_AND_WEAR"
    },
    {
        "airports_cityCode": "KERRY",
        "airports_coordinates_latitude": "52.1809",
        "airports_coordinates_longitude": "-9.52378",
        "airports_countryCode": "ie",
        "airports_iataCode": "KIR",
        "airports_name": "Kerry",
        "airports_regionCode": "MUNSTER"
    },
    {
        "airports_cityCode": "SAN_JUAN",
        "airports_coordinates_latitude": "18.2621",
        "airports_coordinates_longitude": "-66.0007",
        "airports_countryCode": "pr",
        "airports_iataCode": "SJU",
        "airports_name": "San Juan",
        "airports_regionCode": "PUERTO_RICO_NORTH"
    },
    {
        "airports_cityCode": "TOURS",
        "airports_coordinates_latitude": "47.4322",
        "airports_coordinates_longitude": "0.727606",
        "airports_countryCode": "fr",
        "airports_iataCode": "TUF",
        "airports_name": "Tours Loire Valley",
        "airports_regionCode": "CENTRE"
    },
    {
        "airports_cityCode": "SANTA_CRUZ",
        "airports_coordinates_latitude": "-17.3841",
        "airports_coordinates_longitude": "-63.0807",
        "airports_countryCode": "bo",
        "airports_iataCode": "VVI",
        "airports_name": "Santa Cruz",
        "airports_regionCode": "SANTA_CRUZ"
    },
    {
        "airports_cityCode": "MUNICH",
        "airports_coordinates_latitude": "47.9888",
        "airports_coordinates_longitude": "10.2395",
        "airports_countryCode": "de",
        "airports_iataCode": "FMM",
        "airports_name": "Memmingen",
        "airports_regionCode": "SWABIA"
    },
    {
        "airports_cityCode": "EDINBURGH",
        "airports_coordinates_latitude": "55.95",
        "airports_coordinates_longitude": "-3.3725",
        "airports_countryCode": "gb",
        "airports_iataCode": "EDI",
        "airports_name": "Edinburgh",
        "airports_regionCode": "EDINBURGH"
    },
    {
        "airports_cityCode": "CARCASSONNE",
        "airports_coordinates_latitude": "43.216",
        "airports_coordinates_longitude": "2.30632",
        "airports_countryCode": "fr",
        "airports_iataCode": "CCF",
        "airports_name": "Carcassonne",
        "airports_regionCode": "LANGUEDOC-ROUSSILLON"
    },
    {
        "airports_cityCode": "FIGARI",
        "airports_coordinates_latitude": "41.5006",
        "airports_coordinates_longitude": "9.09778",
        "airports_countryCode": "fr",
        "airports_iataCode": "FSC",
        "airports_name": "Figari",
        "airports_regionCode": "CORSICA"
    },
    {
        "airports_cityCode": "BILLUND",
        "airports_coordinates_latitude": "55.7403",
        "airports_coordinates_longitude": "9.15178",
        "airports_countryCode": "dk",
        "airports_iataCode": "BLL",
        "airports_name": "Billund",
        "airports_regionCode": "SOUTHERN_DENMARK"
    },
    {
        "airports_cityCode": "RABAT",
        "airports_coordinates_latitude": "34.0515",
        "airports_coordinates_longitude": "-6.75152",
        "airports_countryCode": "ma",
        "airports_iataCode": "RBA",
        "airports_name": "Rabat",
        "airports_regionCode": "RABAT-SALE-KENITRA"
    },
    {
        "airports_cityCode": "AMSTERDAM",
        "airports_coordinates_latitude": "52.3105",
        "airports_coordinates_longitude": "4.76827",
        "airports_countryCode": "nl",
        "airports_iataCode": "AMS",
        "airports_name": "Amsterdam",
        "airports_regionCode": "DEFAULT_NL"
    },
    {
        "airports_cityCode": "RIJEKA",
        "airports_coordinates_latitude": "45.2169",
        "airports_coordinates_longitude": "14.5703",
        "airports_countryCode": "hr",
        "airports_iataCode": "RJK",
        "airports_name": "Rijeka",
        "airports_regionCode": "KVARNER_BAY"
    },
    {
        "airports_cityCode": "DINARD",
        "airports_coordinates_latitude": "48.5877",
        "airports_coordinates_longitude": "-2.07996",
        "airports_countryCode": "fr",
        "airports_iataCode": "DNR",
        "airports_name": "Dinard",
        "airports_regionCode": "BRITTANY"
    },
    {
        "airports_cityCode": "EILAT",
        "airports_coordinates_latitude": "29.9402",
        "airports_coordinates_longitude": "34.9358",
        "airports_countryCode": "il",
        "airports_iataCode": "VDA",
        "airports_name": "Eilat",
        "airports_regionCode": "DEFAULT_IL"
    },
    {
        "airports_cityCode": "BELFAST",
        "airports_coordinates_latitude": "54.6575",
        "airports_coordinates_longitude": "-6.2158",
        "airports_countryCode": "gb",
        "airports_iataCode": "BFS",
        "airports_name": "Belfast International",
        "airports_regionCode": "DEFAULT_GB"
    },
    {
        "airports_cityCode": "MARSEILLE",
        "airports_coordinates_latitude": "43.4393",
        "airports_coordinates_longitude": "5.22142",
        "airports_countryCode": "fr",
        "airports_iataCode": "MRS",
        "airports_name": "Marseille",
        "airports_regionCode": "PROVENCE-ALPES-COTE_DAZUR_FRENCH_RIVIERA"
    },
    {
        "airports_cityCode": "LEEDS",
        "airports_coordinates_latitude": "53.8659",
        "airports_coordinates_longitude": "-1.66057",
        "airports_countryCode": "gb",
        "airports_iataCode": "LBA",
        "airports_name": "Leeds Bradford",
        "airports_regionCode": "WEST_YORKSHIRE"
    },
    {
        "airports_cityCode": "BRIVE",
        "airports_coordinates_latitude": "45.1508",
        "airports_coordinates_longitude": "1.46917",
        "airports_countryCode": "fr",
        "airports_iataCode": "BVE",
        "airports_name": "Brive",
        "airports_regionCode": "DEFAULT_FR"
    },
    {
        "airports_cityCode": "SZCZECIN",
        "airports_coordinates_latitude": "53.5847",
        "airports_coordinates_longitude": "14.9022",
        "airports_countryCode": "pl",
        "airports_iataCode": "SZZ",
        "airports_name": "Szczecin",
        "airports_regionCode": "POMERANIA"
    },
    {
        "airports_cityCode": "TENERIFE",
        "airports_coordinates_latitude": "28.0445",
        "airports_coordinates_longitude": "-16.5725",
        "airports_countryCode": "es",
        "airports_iataCode": "TFS",
        "airports_name": "Tenerife South",
        "airports_regionCode": "CANARY_ISLES"
    },
    {
        "airports_cityCode": "KEFALONIA",
        "airports_coordinates_latitude": "38.1201",
        "airports_coordinates_longitude": "20.5005",
        "airports_countryCode": "gr",
        "airports_iataCode": "EFL",
        "airports_name": "Kefalonia",
        "airports_regionCode": "IONIAN_ISLANDS_GREEK_ISLANDS"
    },
    {
        "airports_cityCode": "MENORCA",
        "airports_coordinates_latitude": "39.8626",
        "airports_coordinates_longitude": "4.21865",
        "airports_countryCode": "es",
        "airports_iataCode": "MAH",
        "airports_name": "Menorca",
        "airports_regionCode": "BALEARIC_ISLANDS"
    },
    {
        "airports_cityCode": "MALMO",
        "airports_coordinates_latitude": "55.5363",
        "airports_coordinates_longitude": "13.3762",
        "airports_countryCode": "se",
        "airports_iataCode": "MMX",
        "airports_name": "Malmo",
        "airports_regionCode": "DEFAULT_SE"
    },
    {
        "airports_cityCode": "VIGO",
        "airports_coordinates_latitude": "42.23",
        "airports_coordinates_longitude": "-8.63",
        "airports_countryCode": "es",
        "airports_iataCode": "VGO",
        "airports_name": "Vigo",
        "airports_regionCode": "GALICIA"
    },
    {
        "airports_cityCode": "STRASBOURG",
        "airports_coordinates_latitude": "48.5383",
        "airports_coordinates_longitude": "7.62823",
        "airports_countryCode": "fr",
        "airports_iataCode": "SXB",
        "airports_name": "Strasbourg",
        "airports_regionCode": "ALSACE"
    },
    {
        "airports_cityCode": "ABERDEEN",
        "airports_coordinates_latitude": "57.2019",
        "airports_coordinates_longitude": "-2.19778",
        "airports_countryCode": "gb",
        "airports_iataCode": "ABZ",
        "airports_name": "Aberdeen",
        "airports_regionCode": "DEFAULT_GB"
    },
    {
        "airports_cityCode": "OLSZTYN",
        "airports_coordinates_latitude": "53.4819",
        "airports_coordinates_longitude": "20.9378",
        "airports_countryCode": "pl",
        "airports_iataCode": "SZY",
        "airports_name": "Olsztyn - Mazury",
        "airports_regionCode": "MASURIA"
    },
    {
        "airports_cityCode": "CAGLIARI",
        "airports_coordinates_latitude": "39.2515",
        "airports_coordinates_longitude": "9.05428",
        "airports_countryCode": "it",
        "airports_iataCode": "CAG",
        "airports_name": "Cagliari",
        "airports_regionCode": "SARDINIA"
    },
    {
        "airports_cityCode": "AALBORG",
        "airports_coordinates_latitude": "57.0534",
        "airports_coordinates_longitude": "9.5057",
        "airports_countryCode": "dk",
        "airports_iataCode": "AAL",
        "airports_name": "Aalborg",
        "airports_regionCode": "NORTH_DENMARK"
    },
    {
        "airports_cityCode": "ORADEA",
        "airports_coordinates_latitude": "47.0252991",
        "airports_coordinates_longitude": "21.9025002",
        "airports_countryCode": "ro",
        "airports_iataCode": "OMR",
        "airports_name": "Oradea",
        "airports_regionCode": "DEFAULT_RO"
    },
    {
        "airports_cityCode": "STUTTGART",
        "airports_coordinates_latitude": "48.69",
        "airports_coordinates_longitude": "9.2219",
        "airports_countryCode": "de",
        "airports_iataCode": "STR",
        "airports_name": "Stuttgart",
        "airports_regionCode": "BADEN-WURTTEMBERG"
    },
    {
        "airports_cityCode": "LILLE",
        "airports_coordinates_latitude": "50.5619",
        "airports_coordinates_longitude": "3.08944",
        "airports_countryCode": "fr",
        "airports_iataCode": "LIL",
        "airports_name": "Lille",
        "airports_regionCode": "NORD-PAS-DE-CALAIS"
    },
    {
        "airports_cityCode": "MUNICH",
        "airports_coordinates_latitude": "48.3539",
        "airports_coordinates_longitude": "11.7861",
        "airports_countryCode": "de",
        "airports_iataCode": "MUC",
        "airports_name": "Munich",
        "airports_regionCode": "SWABIA"
    },
    {
        "airports_cityCode": "PUNTA_CANA",
        "airports_coordinates_latitude": "18.34",
        "airports_coordinates_longitude": "-68.2107",
        "airports_countryCode": "do",
        "airports_iataCode": "PUJ",
        "airports_name": "Punta Cana",
        "airports_regionCode": "DOMINICAN_ESTE"
    },
    {
        "airports_cityCode": "VARNA",
        "airports_coordinates_latitude": "43.1355",
        "airports_coordinates_longitude": "27.4931",
        "airports_countryCode": "bg",
        "airports_iataCode": "VAR",
        "airports_name": "Varna",
        "airports_regionCode": "DEFAULT_BG"
    },
    {
        "airports_cityCode": "ALGARVE",
        "airports_coordinates_latitude": "37.0144",
        "airports_coordinates_longitude": "-7.96591",
        "airports_countryCode": "pt",
        "airports_iataCode": "FAO",
        "airports_name": "Faro",
        "airports_regionCode": "ALGARVE"
    },
    {
        "airports_cityCode": "FRANKFURT",
        "airports_coordinates_latitude": "50.02",
        "airports_coordinates_longitude": "8.3414",
        "airports_countryCode": "de",
        "airports_iataCode": "FRA",
        "airports_name": "Frankfurt International",
        "airports_regionCode": "DEFAULT_DE"
    },
    {
        "airports_cityCode": "MURCIA",
        "airports_coordinates_latitude": "37.775",
        "airports_coordinates_longitude": "-0.812389",
        "airports_countryCode": "es",
        "airports_iataCode": "MJV",
        "airports_name": "Murcia",
        "airports_regionCode": "COSTA_CALIDA"
    },
    {
        "airports_cityCode": "DOLE",
        "airports_coordinates_latitude": "47.039",
        "airports_coordinates_longitude": "5.42725",
        "airports_countryCode": "fr",
        "airports_iataCode": "DLE",
        "airports_name": "Dole",
        "airports_regionCode": "FRANCHE-COMTE"
    },
    {
        "airports_cityCode": "LAMEZIA",
        "airports_coordinates_latitude": "38.9054",
        "airports_coordinates_longitude": "16.2423",
        "airports_countryCode": "it",
        "airports_iataCode": "SUF",
        "airports_name": "Lamezia",
        "airports_regionCode": "CALABRIA"
    },
    {
        "airports_cityCode": "SAN_PEDRO_SULA",
        "airports_coordinates_latitude": "15.271",
        "airports_coordinates_longitude": "-87.5525",
        "airports_countryCode": "hn",
        "airports_iataCode": "SAP",
        "airports_name": "San Pedro Sula",
        "airports_regionCode": "HONDURAS_CENTRAL_HIGHLANDS"
    },
    {
        "airports_cityCode": "MAASTRICHT",
        "airports_coordinates_latitude": "50.9117",
        "airports_coordinates_longitude": "5.77014",
        "airports_countryCode": "nl",
        "airports_iataCode": "MST",
        "airports_name": "Maastricht",
        "airports_regionCode": "LIMBURG"
    },
    {
        "airports_cityCode": "ZADAR",
        "airports_coordinates_latitude": "44.1083",
        "airports_coordinates_longitude": "15.3467",
        "airports_countryCode": "hr",
        "airports_iataCode": "ZAD",
        "airports_name": "Zadar",
        "airports_regionCode": "DALMATIAN"
    },
    {
        "airports_cityCode": "LOURDES",
        "airports_coordinates_latitude": "43.1787",
        "airports_coordinates_longitude": "-0.006439",
        "airports_countryCode": "fr",
        "airports_iataCode": "LDE",
        "airports_name": "Lourdes",
        "airports_regionCode": "MIDI-PYRENEES"
    },
    {
        "airports_cityCode": "SOFIA",
        "airports_coordinates_latitude": "42.67",
        "airports_coordinates_longitude": "23.35",
        "airports_countryCode": "bg",
        "airports_iataCode": "SOF",
        "airports_name": "Sofia",
        "airports_regionCode": "DEFAULT_BG"
    },
    {
        "airports_cityCode": "SANTO_DOMINGO",
        "airports_coordinates_latitude": "18.2546",
        "airports_coordinates_longitude": "-69.4008",
        "airports_countryCode": "do",
        "airports_iataCode": "SDQ",
        "airports_name": "Santo Domingo",
        "airports_regionCode": "DOMINICAN_ESTE"
    },
    {
        "airports_cityCode": "ANCONA",
        "airports_coordinates_latitude": "43.6163",
        "airports_coordinates_longitude": "13.3623",
        "airports_countryCode": "it",
        "airports_iataCode": "AOI",
        "airports_name": "Ancona",
        "airports_regionCode": "MARCHE"
    },
    {
        "airports_cityCode": "TIMISOARA",
        "airports_coordinates_latitude": "45.81",
        "airports_coordinates_longitude": "21.3381",
        "airports_countryCode": "ro",
        "airports_iataCode": "TSR",
        "airports_name": "Timisoara",
        "airports_regionCode": "BANAT"
    },
    {
        "airports_cityCode": "VILNIUS",
        "airports_coordinates_latitude": "54.6341",
        "airports_coordinates_longitude": "25.2858",
        "airports_countryCode": "lt",
        "airports_iataCode": "VNO",
        "airports_name": "Vilnius",
        "airports_regionCode": "VILNIUS"
    },
    {
        "airports_cityCode": "VENICE",
        "airports_coordinates_latitude": "45.5053",
        "airports_coordinates_longitude": "12.3519",
        "airports_countryCode": "it",
        "airports_iataCode": "VCE",
        "airports_name": "Venice M.Polo",
        "airports_regionCode": "VENETO"
    },
    {
        "airports_cityCode": "BRNO",
        "airports_coordinates_latitude": "49.1513",
        "airports_coordinates_longitude": "16.6944",
        "airports_countryCode": "cz",
        "airports_iataCode": "BRQ",
        "airports_name": "Brno",
        "airports_regionCode": "SOUTH_MORAVIAN"
    },
    {
        "airports_cityCode": "VENICE",
        "airports_coordinates_latitude": "45.6484",
        "airports_coordinates_longitude": "12.1944",
        "airports_countryCode": "it",
        "airports_iataCode": "TSF",
        "airports_name": "Venice Treviso",
        "airports_regionCode": "VENETO"
    },
    {
        "airports_cityCode": "BADEN_BADEN",
        "airports_coordinates_latitude": "48.7794",
        "airports_coordinates_longitude": "8.0805",
        "airports_countryCode": "de",
        "airports_iataCode": "FKB",
        "airports_name": "Karlsruhe/Baden-Baden",
        "airports_regionCode": "BADEN-WURTTEMBERG"
    },
    {
        "airports_cityCode": "TERCEIRA",
        "airports_coordinates_latitude": "38.761944",
        "airports_coordinates_longitude": "-27.090833",
        "airports_countryCode": "pt",
        "airports_iataCode": "TER",
        "airports_name": "Terceira Lajes",
        "airports_regionCode": "AZORES"
    },
    {
        "airports_cityCode": "BREST",
        "airports_coordinates_latitude": "48.4479",
        "airports_coordinates_longitude": "-4.41854",
        "airports_countryCode": "fr",
        "airports_iataCode": "BES",
        "airports_name": "Brest",
        "airports_regionCode": "BRITTANY"
    },
    {
        "airports_cityCode": "RODEZ",
        "airports_coordinates_latitude": "44.4079",
        "airports_coordinates_longitude": "2.48267",
        "airports_countryCode": "fr",
        "airports_iataCode": "RDZ",
        "airports_name": "Rodez",
        "airports_regionCode": "MIDI-PYRENEES"
    },
    {
        "airports_cityCode": "BUENOS_AIRES",
        "airports_coordinates_latitude": "34.492",
        "airports_coordinates_longitude": "-58.3209",
        "airports_countryCode": "ar",
        "airports_iataCode": "EZE",
        "airports_name": "Buenos Aires",
        "airports_regionCode": "PAMPAS"
    },
    {
        "airports_cityCode": "LUBLIN",
        "airports_coordinates_latitude": "51.2319",
        "airports_coordinates_longitude": "22.6903",
        "airports_countryCode": "pl",
        "airports_iataCode": "LUZ",
        "airports_name": "Lublin",
        "airports_regionCode": "LUBLIN"
    },
    {
        "airports_cityCode": "MANCHESTER",
        "airports_coordinates_latitude": "53.3537",
        "airports_coordinates_longitude": "-2.27495",
        "airports_countryCode": "gb",
        "airports_iataCode": "MAN",
        "airports_name": "Manchester",
        "airports_regionCode": "GREATER_MANCHESTER"
    },
    {
        "airports_cityCode": "BOGOTA",
        "airports_coordinates_latitude": "4.4205",
        "airports_coordinates_longitude": "74.0849",
        "airports_countryCode": "co",
        "airports_iataCode": "BOG",
        "airports_name": "Bogota",
        "airports_regionCode": "COLOMBIA_CAPITAL"
    },
    {
        "airports_cityCode": "PALMA",
        "airports_coordinates_latitude": "39.5517",
        "airports_coordinates_longitude": "2.73881",
        "airports_countryCode": "es",
        "airports_iataCode": "PMI",
        "airports_name": "Mallorca",
        "airports_regionCode": "DEFAULT_ES"
    },
    {
        "airports_cityCode": "ASUNCION",
        "airports_coordinates_latitude": "25.1423",
        "airports_coordinates_longitude": "57.3109",
        "airports_countryCode": "py",
        "airports_iataCode": "ASU",
        "airports_name": "Asuncion",
        "airports_regionCode": "PARAGUAY_CENTRAL"
    },
    {
        "airports_cityCode": "SALZBURG",
        "airports_coordinates_latitude": "47.7933",
        "airports_coordinates_longitude": "13.0043",
        "airports_countryCode": "at",
        "airports_iataCode": "SZG",
        "airports_name": "Salzburg",
        "airports_regionCode": "SALZBURG"
    },
    {
        "airports_cityCode": "CORK",
        "airports_coordinates_latitude": "51.8413",
        "airports_coordinates_longitude": "-8.49111",
        "airports_countryCode": "ie",
        "airports_iataCode": "ORK",
        "airports_name": "Cork",
        "airports_regionCode": "MUNSTER"
    },
    {
        "airports_cityCode": "BARCELONA",
        "airports_coordinates_latitude": "41.901",
        "airports_coordinates_longitude": "2.76055",
        "airports_countryCode": "es",
        "airports_iataCode": "GRO",
        "airports_name": "Barcelona Girona",
        "airports_regionCode": "COSTA_BRAVA"
    },
    {
        "airports_cityCode": "VALENCIA",
        "airports_coordinates_latitude": "39.4893",
        "airports_coordinates_longitude": "-0.481625",
        "airports_countryCode": "es",
        "airports_iataCode": "VLC",
        "airports_name": "Valencia",
        "airports_regionCode": "COSTA_AZAHAR"
    },
    {
        "airports_cityCode": "PORTO",
        "airports_coordinates_latitude": "41.2481",
        "airports_coordinates_longitude": "-8.68139",
        "airports_countryCode": "pt",
        "airports_iataCode": "OPO",
        "airports_name": "Porto",
        "airports_regionCode": "DEFAULT_PT"
    },
    {
        "airports_cityCode": "MILAN",
        "airports_coordinates_latitude": "45.63",
        "airports_coordinates_longitude": "8.7231",
        "airports_countryCode": "it",
        "airports_iataCode": "MXP",
        "airports_name": "Milan Malpensa",
        "airports_regionCode": "LOMBARDY"
    },
    {
        "airports_cityCode": "RZESZOW",
        "airports_coordinates_latitude": "50.11",
        "airports_coordinates_longitude": "22.019",
        "airports_countryCode": "pl",
        "airports_iataCode": "RZE",
        "airports_name": "Rzeszow",
        "airports_regionCode": "PODKARPACKIE"
    },
    {
        "airports_cityCode": "MALAGA",
        "airports_coordinates_latitude": "36.6749",
        "airports_coordinates_longitude": "-4.49911",
        "airports_countryCode": "es",
        "airports_iataCode": "AGP",
        "airports_name": "Malaga",
        "airports_regionCode": "COSTA_DE_SOL"
    },
    {
        "airports_cityCode": "PULA",
        "airports_coordinates_latitude": "44.8935",
        "airports_coordinates_longitude": "13.9222",
        "airports_countryCode": "hr",
        "airports_iataCode": "PUY",
        "airports_name": "Pula",
        "airports_regionCode": "DEFAULT_HR"
    },
    {
        "airports_cityCode": "CLERMONT_FERRAND",
        "airports_coordinates_latitude": "45.7867",
        "airports_coordinates_longitude": "3.16917",
        "airports_countryCode": "fr",
        "airports_iataCode": "CFE",
        "airports_name": "Clermont",
        "airports_regionCode": "AUVERGNE"
    },
    {
        "airports_cityCode": "PARMA",
        "airports_coordinates_latitude": "44.8245",
        "airports_coordinates_longitude": "10.2964",
        "airports_countryCode": "it",
        "airports_iataCode": "PMF",
        "airports_name": "Parma",
        "airports_regionCode": "EMILIA-ROMAGNA"
    },
    {
        "airports_cityCode": "BOLOGNA",
        "airports_coordinates_latitude": "44.5354",
        "airports_coordinates_longitude": "11.2887",
        "airports_countryCode": "it",
        "airports_iataCode": "BLQ",
        "airports_name": "Bologna",
        "airports_regionCode": "EMILIA-ROMAGNA"
    },
    {
        "airports_cityCode": "CATANIA",
        "airports_coordinates_latitude": "37.4668",
        "airports_coordinates_longitude": "15.0664",
        "airports_countryCode": "it",
        "airports_iataCode": "CTA",
        "airports_name": "Catania",
        "airports_regionCode": "SICILY"
    },
    {
        "airports_cityCode": "TOULOUSE",
        "airports_coordinates_latitude": "43.6044",
        "airports_coordinates_longitude": "1.4439",
        "airports_countryCode": "fr",
        "airports_iataCode": "TLS",
        "airports_name": "Toulouse",
        "airports_regionCode": "MIDI-PYRENEES"
    },
    {
        "airports_cityCode": "VAXJO",
        "airports_coordinates_latitude": "56.9291",
        "airports_coordinates_longitude": "14.728",
        "airports_countryCode": "se",
        "airports_iataCode": "VXO",
        "airports_name": "Växjö Småland",
        "airports_regionCode": "KRONOBERG"
    },
    {
        "airports_cityCode": "PARIS",
        "airports_coordinates_latitude": "48.7761",
        "airports_coordinates_longitude": "4.18449",
        "airports_countryCode": "fr",
        "airports_iataCode": "XCR",
        "airports_name": "Paris Vatry",
        "airports_regionCode": "PICARDY"
    },
    {
        "airports_cityCode": "FEZ",
        "airports_coordinates_latitude": "33.9273",
        "airports_coordinates_longitude": "-4.97796",
        "airports_countryCode": "ma",
        "airports_iataCode": "FEZ",
        "airports_name": "Fez",
        "airports_regionCode": "FES-MEKNES"
    },
    {
        "airports_cityCode": "GDANSK",
        "airports_coordinates_latitude": "54.3776",
        "airports_coordinates_longitude": "18.4662",
        "airports_countryCode": "pl",
        "airports_iataCode": "GDN",
        "airports_name": "Gdansk",
        "airports_regionCode": "POMERANIA"
    },
    {
        "airports_cityCode": "CANCUN",
        "airports_coordinates_latitude": "49.1513",
        "airports_coordinates_longitude": "16.6944",
        "airports_countryCode": "mx",
        "airports_iataCode": "CUN",
        "airports_name": "Cancun",
        "airports_regionCode": "DEFAULT_MX"
    },
    {
        "airports_cityCode": "ALGHERO",
        "airports_coordinates_latitude": "40.6321",
        "airports_coordinates_longitude": "8.29077",
        "airports_countryCode": "it",
        "airports_iataCode": "AHO",
        "airports_name": "Alghero",
        "airports_regionCode": "SARDINIA"
    },
    {
        "airports_cityCode": "DUSSELDORF",
        "airports_coordinates_latitude": "51.6024",
        "airports_coordinates_longitude": "6.14217",
        "airports_countryCode": "de",
        "airports_iataCode": "NRN",
        "airports_name": "Dusseldorf Weeze",
        "airports_regionCode": "NORTH_RHINE-WESTPHALIA"
    },
    {
        "airports_cityCode": "TURIN",
        "airports_coordinates_latitude": "45.2008",
        "airports_coordinates_longitude": "7.64963",
        "airports_countryCode": "it",
        "airports_iataCode": "TRN",
        "airports_name": "Turin",
        "airports_regionCode": "PIEDMONT"
    },
    {
        "airports_cityCode": "OUJDA",
        "airports_coordinates_latitude": "34.7872",
        "airports_coordinates_longitude": "-1.92399",
        "airports_countryCode": "ma",
        "airports_iataCode": "OUD",
        "airports_name": "Oujda",
        "airports_regionCode": "ORIENTAL-RIF"
    },
    {
        "airports_cityCode": "BERGERAC",
        "airports_coordinates_latitude": "44.8253",
        "airports_coordinates_longitude": "0.518611",
        "airports_countryCode": "fr",
        "airports_iataCode": "EGC",
        "airports_name": "Bergerac",
        "airports_regionCode": "AQUITAINE"
    },
    {
        "airports_cityCode": "GLASGOW",
        "airports_coordinates_latitude": "55.67194",
        "airports_coordinates_longitude": "-4.43306",
        "airports_countryCode": "gb",
        "airports_iataCode": "GLA",
        "airports_name": "Glasgow",
        "airports_regionCode": "LANARKSHIRE"
    },
    {
        "airports_cityCode": "TENERIFE",
        "airports_coordinates_latitude": "28.4827",
        "airports_coordinates_longitude": "-16.3415",
        "airports_countryCode": "es",
        "airports_iataCode": "TFN",
        "airports_name": "Tenerife North",
        "airports_regionCode": "CANARY_ISLES"
    },
    {
        "airports_cityCode": "ALMERIA",
        "airports_coordinates_latitude": "36.8439",
        "airports_coordinates_longitude": "-2.3701",
        "airports_countryCode": "es",
        "airports_iataCode": "LEI",
        "airports_name": "Almeria",
        "airports_regionCode": "ANDALUSIA"
    },
    {
        "airports_cityCode": "BARI",
        "airports_coordinates_latitude": "41.1389",
        "airports_coordinates_longitude": "16.7606",
        "airports_countryCode": "it",
        "airports_iataCode": "BRI",
        "airports_name": "Bari",
        "airports_regionCode": "PUGLIA"
    },
    {
        "airports_cityCode": "BRUSSELS",
        "airports_coordinates_latitude": "50.9014",
        "airports_coordinates_longitude": "4.48444",
        "airports_countryCode": "be",
        "airports_iataCode": "BRU",
        "airports_name": "Brussels",
        "airports_regionCode": "WALLONIA"
    },
    {
        "airports_cityCode": "PERUGIA",
        "airports_coordinates_latitude": "43.0959",
        "airports_coordinates_longitude": "12.5132",
        "airports_countryCode": "it",
        "airports_iataCode": "PEG",
        "airports_name": "Perugia",
        "airports_regionCode": "UMBRIA"
    },
    {
        "airports_cityCode": "VALLADOLID",
        "airports_coordinates_latitude": "41.7061",
        "airports_coordinates_longitude": "-4.85194",
        "airports_countryCode": "es",
        "airports_iataCode": "VLL",
        "airports_name": "Valladolid",
        "airports_regionCode": "CASTILE-LEON"
    },
    {
        "airports_cityCode": "WARSAW",
        "airports_coordinates_latitude": "52.1657",
        "airports_coordinates_longitude": "20.9671",
        "airports_countryCode": "pl",
        "airports_iataCode": "WAW",
        "airports_name": "Warsaw Chopin",
        "airports_regionCode": "VOIVODSHIP"
    },
    {
        "airports_cityCode": "LISBON",
        "airports_coordinates_latitude": "38.7813",
        "airports_coordinates_longitude": "-9.13592",
        "airports_countryCode": "pt",
        "airports_iataCode": "LIS",
        "airports_name": "Lisbon",
        "airports_regionCode": "LISBON"
    },
    {
        "airports_cityCode": "LIVERPOOL",
        "airports_coordinates_latitude": "53.3336",
        "airports_coordinates_longitude": "-2.84972",
        "airports_countryCode": "gb",
        "airports_iataCode": "LPL",
        "airports_name": "Liverpool",
        "airports_regionCode": "MERSEYSIDE"
    },
    {
        "airports_cityCode": "LYON",
        "airports_coordinates_latitude": "45.7256",
        "airports_coordinates_longitude": "5.0811",
        "airports_countryCode": "fr",
        "airports_iataCode": "LYS",
        "airports_name": "Lyon",
        "airports_regionCode": "RHONE-ALPES"
    },
    {
        "airports_cityCode": "NEWQUAY",
        "airports_coordinates_latitude": "50.4406",
        "airports_coordinates_longitude": "-4.99541",
        "airports_countryCode": "gb",
        "airports_iataCode": "NQY",
        "airports_name": "Newquay Cornwall",
        "airports_regionCode": "DEFAULT_GB"
    },
    {
        "airports_cityCode": "ZARAGOZA",
        "airports_coordinates_latitude": "41.6662",
        "airports_coordinates_longitude": "-1.04155",
        "airports_countryCode": "es",
        "airports_iataCode": "ZAZ",
        "airports_name": "Zaragoza",
        "airports_regionCode": "ARAGON"
    },
    {
        "airports_cityCode": "MONTEVIDEO",
        "airports_coordinates_latitude": "-34.5018",
        "airports_coordinates_longitude": "-56.0151",
        "airports_countryCode": "uy",
        "airports_iataCode": "MVD",
        "airports_name": "Montevideo",
        "airports_regionCode": "GREATER_MONTEVIDEO"
    },
    {
        "airports_cityCode": "BARCELONA",
        "airports_coordinates_latitude": "41.1474",
        "airports_coordinates_longitude": "1.16717",
        "airports_countryCode": "es",
        "airports_iataCode": "REU",
        "airports_name": "Barcelona Reus",
        "airports_regionCode": "COSTA_BRAVA"
    },
    {
        "airports_cityCode": "BIARRITZ",
        "airports_coordinates_latitude": "43.4684",
        "airports_coordinates_longitude": "-1.52332",
        "airports_countryCode": "fr",
        "airports_iataCode": "BIQ",
        "airports_name": "Biarritz",
        "airports_regionCode": "AQUITAINE"
    },
    {
        "airports_cityCode": "BOURNEMOUTH",
        "airports_coordinates_latitude": "50.78",
        "airports_coordinates_longitude": "-1.8425",
        "airports_countryCode": "gb",
        "airports_iataCode": "BOH",
        "airports_name": "Bournemouth",
        "airports_regionCode": "HAMPSHIRE"
    },
    {
        "airports_cityCode": "TRAPANI",
        "airports_coordinates_latitude": "37.9114",
        "airports_coordinates_longitude": "12.488",
        "airports_countryCode": "it",
        "airports_iataCode": "TPS",
        "airports_name": "Trapani",
        "airports_regionCode": "SICILY"
    },
    {
        "airports_cityCode": "PRAGUE",
        "airports_coordinates_latitude": "50.1008",
        "airports_coordinates_longitude": "14.26",
        "airports_countryCode": "cz",
        "airports_iataCode": "PRG",
        "airports_name": "Prague",
        "airports_regionCode": "CENTRAL_BOHEMIAN"
    },
    {
        "airports_cityCode": "LANZAROTE",
        "airports_coordinates_latitude": "28.9455",
        "airports_coordinates_longitude": "-13.6052",
        "airports_countryCode": "es",
        "airports_iataCode": "ACE",
        "airports_name": "Lanzarote",
        "airports_regionCode": "CANARY_ISLES"
    },
    {
        "airports_cityCode": "LONDON",
        "airports_coordinates_latitude": "51.885",
        "airports_coordinates_longitude": "0.235",
        "airports_countryCode": "gb",
        "airports_iataCode": "STN",
        "airports_name": "London Stansted",
        "airports_regionCode": "GREATER_LONDON"
    },
    {
        "airports_cityCode": "AGADIR",
        "airports_coordinates_latitude": "30.325",
        "airports_coordinates_longitude": "-9.41307",
        "airports_countryCode": "ma",
        "airports_iataCode": "AGA",
        "airports_name": "Agadir",
        "airports_regionCode": "SOUSS-MASSA"
    },
    {
        "airports_cityCode": "BREMEN",
        "airports_coordinates_latitude": "53.0475",
        "airports_coordinates_longitude": "8.78667",
        "airports_countryCode": "de",
        "airports_iataCode": "BRE",
        "airports_name": "Bremen",
        "airports_regionCode": "BREMEN-OLDENBURG"
    },
    {
        "airports_cityCode": "AARHUS",
        "airports_coordinates_latitude": "56.3",
        "airports_coordinates_longitude": "10.619",
        "airports_countryCode": "dk",
        "airports_iataCode": "AAR",
        "airports_name": "Aarhus",
        "airports_regionCode": "EAST_JUTLAND"
    },
    {
        "airports_cityCode": "TRIESTE",
        "airports_coordinates_latitude": "45.8275",
        "airports_coordinates_longitude": "13.4722",
        "airports_countryCode": "it",
        "airports_iataCode": "TRS",
        "airports_name": "Trieste",
        "airports_regionCode": "FRIULI-VENEZIA_GIULIA"
    },
    {
        "airports_cityCode": "CORFU",
        "airports_coordinates_latitude": "39.6019",
        "airports_coordinates_longitude": "19.9117",
        "airports_countryCode": "gr",
        "airports_iataCode": "CFU",
        "airports_name": "Corfu",
        "airports_regionCode": "IONIAN_ISLANDS_GREEK_ISLANDS"
    },
    {
        "airports_cityCode": "HAMBURG",
        "airports_coordinates_latitude": "53.63028",
        "airports_coordinates_longitude": "9.99111",
        "airports_countryCode": "de",
        "airports_iataCode": "HAM",
        "airports_name": "Hamburg",
        "airports_regionCode": "METROPOLREGION_HAMBURG"
    },
    {
        "airports_cityCode": "ATHENS",
        "airports_coordinates_latitude": "37.9364",
        "airports_coordinates_longitude": "23.9445",
        "airports_countryCode": "gr",
        "airports_iataCode": "ATH",
        "airports_name": "Athens",
        "airports_regionCode": "DEFAULT_GR"
    },
    {
        "airports_cityCode": "SANTORINI",
        "airports_coordinates_latitude": "36.3992",
        "airports_coordinates_longitude": "25.4793",
        "airports_countryCode": "gr",
        "airports_iataCode": "JTR",
        "airports_name": "Santorini",
        "airports_regionCode": "SANTORINI"
    },
    {
        "airports_cityCode": "ST_ETIENNE",
        "airports_coordinates_latitude": "45.5406",
        "airports_coordinates_longitude": "4.29639",
        "airports_countryCode": "fr",
        "airports_iataCode": "EBU",
        "airports_name": "St Etienne",
        "airports_regionCode": "RHONE-ALPES"
    },
    {
        "airports_cityCode": "LISBON",
        "airports_coordinates_latitude": "37.74194",
        "airports_coordinates_longitude": "-25.69778",
        "airports_countryCode": "pt",
        "airports_iataCode": "PDL",
        "airports_name": "Ponta Delgada",
        "airports_regionCode": "LISBON"
    },
    {
        "airports_cityCode": "PARDUBICE",
        "airports_coordinates_latitude": "50.0048",
        "airports_coordinates_longitude": "15.4419",
        "airports_countryCode": "cz",
        "airports_iataCode": "PED",
        "airports_name": "Pardubice",
        "airports_regionCode": "EAST_BOHEMIAN"
    },
    {
        "airports_cityCode": "BERLIN",
        "airports_coordinates_latitude": "52.38",
        "airports_coordinates_longitude": "13.5225",
        "airports_countryCode": "de",
        "airports_iataCode": "SXF",
        "airports_name": "Berlin Schönefeld",
        "airports_regionCode": "BERLIN-BRANDENBURG"
    },
    {
        "airports_cityCode": "LUXEMBOURG",
        "airports_coordinates_latitude": "49.6233",
        "airports_coordinates_longitude": "6.2044",
        "airports_countryCode": "lu",
        "airports_iataCode": "LUX",
        "airports_name": "Luxembourg",
        "airports_regionCode": "DEFAULT_LU"
    },
    {
        "airports_cityCode": "PODGORICA",
        "airports_coordinates_latitude": "42.3594",
        "airports_coordinates_longitude": "19.2519",
        "airports_countryCode": "me",
        "airports_iataCode": "TGD",
        "airports_name": "Podgorica",
        "airports_regionCode": "DEFAULT_ME"
    },
    {
        "airports_cityCode": "THESSALONIKI",
        "airports_coordinates_latitude": "40.5197",
        "airports_coordinates_longitude": "22.9709",
        "airports_countryCode": "gr",
        "airports_iataCode": "SKG",
        "airports_name": "Thessaloniki",
        "airports_regionCode": "CENTRAL_MACEDONIA"
    },
    {
        "airports_cityCode": "NANTES",
        "airports_coordinates_latitude": "47.1532",
        "airports_coordinates_longitude": "-1.61073",
        "airports_countryCode": "fr",
        "airports_iataCode": "NTE",
        "airports_name": "Nantes",
        "airports_regionCode": "PAYS_DE_LA_LOIRE"
    },
    {
        "airports_cityCode": "PAPHOS",
        "airports_coordinates_latitude": "34.718",
        "airports_coordinates_longitude": "32.4857",
        "airports_countryCode": "cy",
        "airports_iataCode": "PFO",
        "airports_name": "Paphos",
        "airports_regionCode": "PAPHOS"
    },
    {
        "airports_cityCode": "LEIPZIG",
        "airports_coordinates_latitude": "51.4324",
        "airports_coordinates_longitude": "12.2416",
        "airports_countryCode": "de",
        "airports_iataCode": "LEJ",
        "airports_name": "Leipzig",
        "airports_regionCode": "DEFAULT_DE"
    },
    {
        "airports_cityCode": "BUCHAREST",
        "airports_coordinates_latitude": "44.5722",
        "airports_coordinates_longitude": "26.1022",
        "airports_countryCode": "ro",
        "airports_iataCode": "OTP",
        "airports_name": "Bucharest",
        "airports_regionCode": "BUCHAREST"
    },
    {
        "airports_cityCode": "ROME",
        "airports_coordinates_latitude": "41.7994",
        "airports_coordinates_longitude": "12.5949",
        "airports_countryCode": "it",
        "airports_iataCode": "CIA",
        "airports_name": "Rome Ciampino",
        "airports_regionCode": "LAZIO"
    },
    {
        "airports_cityCode": "SHANNON",
        "airports_coordinates_latitude": "52.702",
        "airports_coordinates_longitude": "-8.92482",
        "airports_countryCode": "ie",
        "airports_iataCode": "SNN",
        "airports_name": "Shannon",
        "airports_regionCode": "MUNSTER"
    },
    {
        "airports_cityCode": "BRUSSELS",
        "airports_coordinates_latitude": "50.4592",
        "airports_coordinates_longitude": "4.45382",
        "airports_countryCode": "be",
        "airports_iataCode": "CRL",
        "airports_name": "Brussels Charleroi",
        "airports_regionCode": "WALLONIA"
    },
    {
        "airports_cityCode": "KAUNAS",
        "airports_coordinates_latitude": "54.9639",
        "airports_coordinates_longitude": "24.0848",
        "airports_countryCode": "lt",
        "airports_iataCode": "KUN",
        "airports_name": "Kaunas",
        "airports_regionCode": "KAUNAS"
    },
    {
        "airports_cityCode": "BRISTOL",
        "airports_coordinates_latitude": "51.3827",
        "airports_coordinates_longitude": "-2.71909",
        "airports_countryCode": "gb",
        "airports_iataCode": "BRS",
        "airports_name": "Bristol",
        "airports_regionCode": "GLOUCESTSHIRE"
    },
    {
        "airports_cityCode": "MILAN",
        "airports_coordinates_latitude": "45.6739",
        "airports_coordinates_longitude": "9.70417",
        "airports_countryCode": "it",
        "airports_iataCode": "BGY",
        "airports_name": "Milan Bergamo",
        "airports_regionCode": "LOMBARDY"
    },
    {
        "airports_cityCode": "EINDHOVEN",
        "airports_coordinates_latitude": "51.4501",
        "airports_coordinates_longitude": "5.37453",
        "airports_countryCode": "nl",
        "airports_iataCode": "EIN",
        "airports_name": "Eindhoven",
        "airports_regionCode": "NORTH_BRABANT"
    },
    {
        "airports_cityCode": "LIMOGES",
        "airports_coordinates_latitude": "45.8628",
        "airports_coordinates_longitude": "1.17944",
        "airports_countryCode": "fr",
        "airports_iataCode": "LIG",
        "airports_name": "Limoges",
        "airports_regionCode": "LIMOUSIN"
    },
    {
        "airports_cityCode": "BIRMINGHAM",
        "airports_coordinates_latitude": "52.4539",
        "airports_coordinates_longitude": "-1.74803",
        "airports_countryCode": "gb",
        "airports_iataCode": "BHX",
        "airports_name": "Birmingham",
        "airports_regionCode": "EAST_MIDLANDS"
    },
    {
        "airports_cityCode": "OSLO",
        "airports_coordinates_latitude": "60.2028",
        "airports_coordinates_longitude": "11.0839",
        "airports_countryCode": "no",
        "airports_iataCode": "OSL",
        "airports_name": "Oslo",
        "airports_regionCode": "OSLO"
    },
    {
        "airports_cityCode": "LINZ",
        "airports_coordinates_latitude": "48.2332",
        "airports_coordinates_longitude": "14.1875",
        "airports_countryCode": "at",
        "airports_iataCode": "LNZ",
        "airports_name": "Linz",
        "airports_regionCode": "UPPER_AUSTRIA"
    },
    {
        "airports_cityCode": "FUERTEVENTURA",
        "airports_coordinates_latitude": "28.4527",
        "airports_coordinates_longitude": "-13.8638",
        "airports_countryCode": "es",
        "airports_iataCode": "FUE",
        "airports_name": "Fuerteventura",
        "airports_regionCode": "CANARY_ISLES"
    },
    {
        "airports_cityCode": "LA_ROCHELLE",
        "airports_coordinates_latitude": "46.1792",
        "airports_coordinates_longitude": "-1.19528",
        "airports_countryCode": "fr",
        "airports_iataCode": "LRH",
        "airports_name": "La Rochelle",
        "airports_regionCode": "POITOU-CHARENTES"
    },
    {
        "airports_cityCode": "BASEL",
        "airports_coordinates_latitude": "47.5896",
        "airports_coordinates_longitude": "7.52991",
        "airports_countryCode": "ch",
        "airports_iataCode": "BSL",
        "airports_name": "Basel",
        "airports_regionCode": "DEFAULT_CH"
    },
    {
        "airports_cityCode": "BENIDORM",
        "airports_coordinates_latitude": "38.2822",
        "airports_coordinates_longitude": "-0.558156",
        "airports_countryCode": "es",
        "airports_iataCode": "ALC",
        "airports_name": "Alicante",
        "airports_regionCode": "COSTA_BLANCA"
    },
    {
        "airports_cityCode": "NIS",
        "airports_coordinates_latitude": "43.3372",
        "airports_coordinates_longitude": "21.8536",
        "airports_countryCode": "rs",
        "airports_iataCode": "INI",
        "airports_name": "Nis",
        "airports_regionCode": "DEFAULT_RS"
    },
    {
        "airports_cityCode": "KRAKOW",
        "airports_coordinates_latitude": "50.0777",
        "airports_coordinates_longitude": "19.7848",
        "airports_countryCode": "pl",
        "airports_iataCode": "KRK",
        "airports_name": "Krakow",
        "airports_regionCode": "MALOPOLSKA"
    },
    {
        "airports_cityCode": "COLOGNE",
        "airports_coordinates_latitude": "50.8659",
        "airports_coordinates_longitude": "7.14274",
        "airports_countryCode": "de",
        "airports_iataCode": "CGN",
        "airports_name": "Cologne",
        "airports_regionCode": "NORTH_RHINE-WESTPHALIA"
    },
    {
        "airports_cityCode": "JEREZ",
        "airports_coordinates_latitude": "36.7446",
        "airports_coordinates_longitude": "-6.06011",
        "airports_countryCode": "es",
        "airports_iataCode": "XRY",
        "airports_name": "Jerez",
        "airports_regionCode": "ANDALUSIA"
    },
    {
        "airports_cityCode": "VITORIA-GASTEIZ",
        "airports_coordinates_latitude": "42.8828",
        "airports_coordinates_longitude": "-2.7244",
        "airports_countryCode": "es",
        "airports_iataCode": "VIT",
        "airports_name": "Vitoria (Basque Country)",
        "airports_regionCode": "DEFAULT_ES"
    },
    {
        "airports_cityCode": "TANGIER",
        "airports_coordinates_latitude": "35.7269",
        "airports_coordinates_longitude": "-5.91689",
        "airports_countryCode": "ma",
        "airports_iataCode": "TNG",
        "airports_name": "Tangier",
        "airports_regionCode": "TANGIER-TETUAN"
    },
    {
        "airports_cityCode": "GENOA",
        "airports_coordinates_latitude": "44.4133",
        "airports_coordinates_longitude": "8.8375",
        "airports_countryCode": "it",
        "airports_iataCode": "GOA",
        "airports_name": "Genoa",
        "airports_regionCode": "LIGURIA"
    },
    {
        "airports_cityCode": "SEVILLE",
        "airports_coordinates_latitude": "37.418",
        "airports_coordinates_longitude": "-5.89311",
        "airports_countryCode": "es",
        "airports_iataCode": "SVQ",
        "airports_name": "Seville",
        "airports_regionCode": "ANDALUSIA"
    },
    {
        "airports_cityCode": "NANTES",
        "airports_coordinates_latitude": "47.7588",
        "airports_coordinates_longitude": "-3.4378",
        "airports_countryCode": "fr",
        "airports_iataCode": "LRT",
        "airports_name": "Lorient",
        "airports_regionCode": "PAYS_DE_LA_LOIRE"
    },
    {
        "airports_cityCode": "NICE",
        "airports_coordinates_latitude": "43.6584",
        "airports_coordinates_longitude": "7.21587",
        "airports_countryCode": "fr",
        "airports_iataCode": "NCE",
        "airports_name": "Nice",
        "airports_regionCode": "PROVENCE-ALPES-COTE_DAZUR_FRENCH_RIVIERA"
    },
    {
        "airports_cityCode": "BARCELONA",
        "airports_coordinates_latitude": "41.2971",
        "airports_coordinates_longitude": "2.07846",
        "airports_countryCode": "es",
        "airports_iataCode": "BCN",
        "airports_name": "Barcelona",
        "airports_regionCode": "COSTA_BRAVA"
    },
    {
        "airports_cityCode": "MALTA",
        "airports_coordinates_latitude": "35.8575",
        "airports_coordinates_longitude": "14.4775",
        "airports_countryCode": "mt",
        "airports_iataCode": "MLA",
        "airports_name": "Malta",
        "airports_regionCode": "MALTA"
    },
    {
        "airports_cityCode": "LARNACA",
        "airports_coordinates_latitude": "34.8751",
        "airports_coordinates_longitude": "33.6249",
        "airports_countryCode": "cy",
        "airports_iataCode": "LCA",
        "airports_name": "Larnaca",
        "airports_regionCode": "DEFAULT_CY"
    },
    {
        "airports_cityCode": "TAMPERE",
        "airports_coordinates_latitude": "61.4141",
        "airports_coordinates_longitude": "23.6044",
        "airports_countryCode": "fi",
        "airports_iataCode": "TMP",
        "airports_name": "Tampere",
        "airports_regionCode": "PIRKANMAA"
    },
    {
        "airports_cityCode": "LIMA",
        "airports_coordinates_latitude": "-12.0119",
        "airports_coordinates_longitude": "-77.0652",
        "airports_countryCode": "pe",
        "airports_iataCode": "LIM",
        "airports_name": "Lima",
        "airports_regionCode": "LIMA"
    },
    {
        "airports_cityCode": "POITIERS",
        "airports_coordinates_latitude": "46.5877",
        "airports_coordinates_longitude": "0.306666",
        "airports_countryCode": "fr",
        "airports_iataCode": "PIS",
        "airports_name": "Poitiers",
        "airports_regionCode": "POITOU-CHARENTES"
    },
    {
        "airports_cityCode": "PISA",
        "airports_coordinates_latitude": "43.6839",
        "airports_coordinates_longitude": "10.3927",
        "airports_countryCode": "it",
        "airports_iataCode": "PSA",
        "airports_name": "Pisa",
        "airports_regionCode": "TUSCANY"
    },
    {
        "airports_cityCode": "FRANKFURT",
        "airports_coordinates_latitude": "49.9487",
        "airports_coordinates_longitude": "7.26389",
        "airports_countryCode": "de",
        "airports_iataCode": "HHN",
        "airports_name": "Frankfurt Hahn",
        "airports_regionCode": "DEFAULT_DE"
    },
    {
        "airports_cityCode": "NUREMBERG",
        "airports_coordinates_latitude": "49.4987",
        "airports_coordinates_longitude": "11.0669",
        "airports_countryCode": "de",
        "airports_iataCode": "NUE",
        "airports_name": "Nuremberg",
        "airports_regionCode": "MIDDLE_FRANCONIA"
    },
    {
        "airports_cityCode": "RHODES",
        "airports_coordinates_latitude": "36.4054",
        "airports_coordinates_longitude": "28.0862",
        "airports_countryCode": "gr",
        "airports_iataCode": "RHO",
        "airports_name": "Rhodes",
        "airports_regionCode": "DODECANESE"
    },
    {
        "airports_cityCode": "OSTRAVA",
        "airports_coordinates_latitude": "49.6963",
        "airports_coordinates_longitude": "18.1111",
        "airports_countryCode": "cz",
        "airports_iataCode": "OSR",
        "airports_name": "Ostrava",
        "airports_regionCode": "MORAVIAN-SILESIAN"
    },
    {
        "airports_cityCode": "BURGAS",
        "airports_coordinates_latitude": "42.3413",
        "airports_coordinates_longitude": "27.3055",
        "airports_countryCode": "bg",
        "airports_iataCode": "BOJ",
        "airports_name": "Burgas",
        "airports_regionCode": "DEFAULT_BG"
    },
    {
        "airports_cityCode": "CARACAS",
        "airports_coordinates_latitude": "10.3611",
        "airports_coordinates_longitude": "66.5926",
        "airports_countryCode": "ve",
        "airports_iataCode": "CCS",
        "airports_name": "Caracas",
        "airports_regionCode": "VENEZUELA_CAPITAL"
    },
    {
        "airports_cityCode": "STOCKHOLM",
        "airports_coordinates_latitude": "59.5894",
        "airports_coordinates_longitude": "16.6336",
        "airports_countryCode": "se",
        "airports_iataCode": "VST",
        "airports_name": "Stockholm Västerås",
        "airports_regionCode": "STOCKHOLM"
    },
    {
        "airports_cityCode": "IBIZA",
        "airports_coordinates_latitude": "38.8729",
        "airports_coordinates_longitude": "1.37312",
        "airports_countryCode": "es",
        "airports_iataCode": "IBZ",
        "airports_name": "Ibiza",
        "airports_regionCode": "BALEARIC_ISLANDS"
    },
    {
        "airports_cityCode": "MIAMI",
        "airports_coordinates_latitude": "25.4736",
        "airports_coordinates_longitude": "-80.1726",
        "airports_countryCode": "us",
        "airports_iataCode": "MIA",
        "airports_name": "Miami",
        "airports_regionCode": "FLORIDA"
    },
    {
        "airports_cityCode": "GALWAY",
        "airports_coordinates_latitude": "53.9103",
        "airports_coordinates_longitude": "-8.81849",
        "airports_countryCode": "ie",
        "airports_iataCode": "NOC",
        "airports_name": "Knock",
        "airports_regionCode": "DEFAULT_IE"
    },
    {
        "airports_cityCode": "HAVANA",
        "airports_coordinates_latitude": "22.5921",
        "airports_coordinates_longitude": "-82.2433",
        "airports_countryCode": "cu",
        "airports_iataCode": "HAV",
        "airports_name": "Havana",
        "airports_regionCode": "HAVANA_CITY"
    },
    {
        "airports_cityCode": "MYKONOS",
        "airports_coordinates_latitude": "37.4351",
        "airports_coordinates_longitude": "25.3481",
        "airports_countryCode": "gr",
        "airports_iataCode": "JMK",
        "airports_name": "Mykonos",
        "airports_regionCode": "IONIAN_ISLANDS_GREEK_ISLANDS"
    },
    {
        "airports_cityCode": "MONTPELLIER",
        "airports_coordinates_latitude": "43.5762",
        "airports_coordinates_longitude": "3.96301",
        "airports_countryCode": "fr",
        "airports_iataCode": "MPL",
        "airports_name": "Montpellier",
        "airports_regionCode": "LANGUEDOC-ROUSSILLON"
    },
    {
        "airports_cityCode": "BUDAPEST",
        "airports_coordinates_latitude": "47.4369",
        "airports_coordinates_longitude": "19.2556",
        "airports_countryCode": "hu",
        "airports_iataCode": "BUD",
        "airports_name": "Budapest",
        "airports_regionCode": "CENTRAL_HUNGARY"
    },
    {
        "airports_cityCode": "GOTHENBURG",
        "airports_coordinates_latitude": "57.6741",
        "airports_coordinates_longitude": "12.2925",
        "airports_countryCode": "se",
        "airports_iataCode": "GOT",
        "airports_name": "Göteborg Landvetter",
        "airports_regionCode": "GOTHENBURG"
    },
    {
        "airports_cityCode": "LONDON",
        "airports_coordinates_latitude": "51.8747",
        "airports_coordinates_longitude": "-0.368333",
        "airports_countryCode": "gb",
        "airports_iataCode": "LTN",
        "airports_name": "London Luton",
        "airports_regionCode": "GREATER_LONDON"
    },
    {
        "airports_cityCode": "GRAN_CANARIA",
        "airports_coordinates_latitude": "27.9319",
        "airports_coordinates_longitude": "-15.3866",
        "airports_countryCode": "es",
        "airports_iataCode": "LPA",
        "airports_name": "Gran Canaria",
        "airports_regionCode": "CANARY_ISLES"
    },
    {
        "airports_cityCode": "BORDEAUX",
        "airports_coordinates_latitude": "44.8283",
        "airports_coordinates_longitude": "-0.715556",
        "airports_countryCode": "fr",
        "airports_iataCode": "BOD",
        "airports_name": "Bordeaux",
        "airports_regionCode": "AQUITAINE"
    },
    {
        "airports_cityCode": "NEW_YORK",
        "airports_coordinates_latitude": "73.4644",
        "airports_coordinates_longitude": "40.3823",
        "airports_countryCode": "us",
        "airports_iataCode": "JFK",
        "airports_name": "New York (JFK)",
        "airports_regionCode": "NEW_YORK"
    },
    {
        "airports_cityCode": "LODZ",
        "airports_coordinates_latitude": "51.7219",
        "airports_coordinates_longitude": "19.3981",
        "airports_countryCode": "pl",
        "airports_iataCode": "LCJ",
        "airports_name": "Lodz",
        "airports_regionCode": "LODZ"
    },
    {
        "airports_cityCode": "PALANGA",
        "airports_coordinates_latitude": "55.9733",
        "airports_coordinates_longitude": "21.0939",
        "airports_countryCode": "lt",
        "airports_iataCode": "PLQ",
        "airports_name": "Palanga",
        "airports_regionCode": "DEFAULT_LT"
    },
    {
        "airports_cityCode": "PESCARA",
        "airports_coordinates_latitude": "42.4317",
        "airports_coordinates_longitude": "14.1811",
        "airports_countryCode": "it",
        "airports_iataCode": "PSR",
        "airports_name": "Pescara",
        "airports_regionCode": "ABRUZZO"
    },
    {
        "airports_cityCode": "WROCLAW",
        "airports_coordinates_latitude": "51.1027",
        "airports_coordinates_longitude": "16.8858",
        "airports_countryCode": "pl",
        "airports_iataCode": "WRO",
        "airports_name": "Wroclaw",
        "airports_regionCode": "LOWER_SILESIAN_VOIVODESHIP"
    },
    {
        "airports_cityCode": "DEAUVILLE",
        "airports_coordinates_latitude": "49.3653",
        "airports_coordinates_longitude": "0.154306",
        "airports_countryCode": "fr",
        "airports_iataCode": "DOL",
        "airports_name": "Deauville",
        "airports_regionCode": "LOWER_NORMANDY"
    },
    {
        "airports_cityCode": "PLOVDIV",
        "airports_coordinates_latitude": "42.0678",
        "airports_coordinates_longitude": "24.8508",
        "airports_countryCode": "bg",
        "airports_iataCode": "PDV",
        "airports_name": "Plovdiv",
        "airports_regionCode": "EASTERN_RUMELIA"
    },
    {
        "airports_cityCode": "PERPIGNAN",
        "airports_coordinates_latitude": "42.7404",
        "airports_coordinates_longitude": "2.87067",
        "airports_countryCode": "fr",
        "airports_iataCode": "PGF",
        "airports_name": "Perpignan",
        "airports_regionCode": "LANGUEDOC-ROUSSILLON"
    },
    {
        "airports_cityCode": "WARSAW",
        "airports_coordinates_latitude": "52.4511",
        "airports_coordinates_longitude": "20.6517",
        "airports_countryCode": "pl",
        "airports_iataCode": "WMI",
        "airports_name": "Warsaw Modlin",
        "airports_regionCode": "VOIVODSHIP"
    },
    {
        "airports_cityCode": "SALVADOR",
        "airports_coordinates_latitude": "-12.5431",
        "airports_coordinates_longitude": "-38.1921",
        "airports_countryCode": "br",
        "airports_iataCode": "SSA",
        "airports_name": "Salvador",
        "airports_regionCode": "BRAZIL_NORTHEAST"
    },
    {
        "airports_cityCode": "NADOR",
        "airports_coordinates_latitude": "34.9888",
        "airports_coordinates_longitude": "-3.02821",
        "airports_countryCode": "ma",
        "airports_iataCode": "NDR",
        "airports_name": "Nador",
        "airports_regionCode": "ORIENTAL-RIF"
    },
    {
        "airports_cityCode": "GLASGOW",
        "airports_coordinates_latitude": "55.5094",
        "airports_coordinates_longitude": "-4.58667",
        "airports_countryCode": "gb",
        "airports_iataCode": "PIK",
        "airports_name": "Glasgow Prestwick",
        "airports_regionCode": "LANARKSHIRE"
    },
    {
        "airports_cityCode": "PARIS",
        "airports_coordinates_latitude": "49.4544",
        "airports_coordinates_longitude": "2.11278",
        "airports_countryCode": "fr",
        "airports_iataCode": "BVA",
        "airports_name": "Paris Beauvais",
        "airports_regionCode": "PICARDY"
    },
    {
        "airports_cityCode": "KATOWICE",
        "airports_coordinates_latitude": "50.4743",
        "airports_coordinates_longitude": "19.08",
        "airports_countryCode": "pl",
        "airports_iataCode": "KTW",
        "airports_name": "Katowice",
        "airports_regionCode": "UPPER_SILESIA"
    },
    {
        "airports_cityCode": "COMISO",
        "airports_coordinates_latitude": "36.9946",
        "airports_coordinates_longitude": "14.6072",
        "airports_countryCode": "it",
        "airports_iataCode": "CIY",
        "airports_name": "Comiso",
        "airports_regionCode": "SICILY"
    },
    {
        "airports_cityCode": "STOCKHOLM",
        "airports_coordinates_latitude": "58.7886",
        "airports_coordinates_longitude": "16.9122",
        "airports_countryCode": "se",
        "airports_iataCode": "NYO",
        "airports_name": "Stockholm Skavsta",
        "airports_regionCode": "STOCKHOLM"
    },
    {
        "airports_cityCode": "RIGA",
        "airports_coordinates_latitude": "56.9236",
        "airports_coordinates_longitude": "23.9711",
        "airports_countryCode": "lv",
        "airports_iataCode": "RIX",
        "airports_name": "Riga",
        "airports_regionCode": "RIGA_PLANNING_REGION"
    },
    {
        "airports_cityCode": "DORTMUND",
        "airports_coordinates_latitude": "51.5183",
        "airports_coordinates_longitude": "7.61224",
        "airports_countryCode": "de",
        "airports_iataCode": "DTM",
        "airports_name": "Dortmund",
        "airports_regionCode": "RHINE-RUHR"
    },
    {
        "airports_cityCode": "BRINDISI",
        "airports_coordinates_latitude": "40.6576",
        "airports_coordinates_longitude": "17.947",
        "airports_countryCode": "it",
        "airports_iataCode": "BDS",
        "airports_name": "Brindisi",
        "airports_regionCode": "PUGLIA"
    },
    {
        "airports_cityCode": "CARDIFF",
        "airports_coordinates_latitude": "51.3967",
        "airports_coordinates_longitude": "-3.34333",
        "airports_countryCode": "gb",
        "airports_iataCode": "CWL",
        "airports_name": "Cardiff",
        "airports_regionCode": "CARDIFF"
    },
    {
        "airports_cityCode": "NAPLES",
        "airports_coordinates_latitude": "40.5304",
        "airports_coordinates_longitude": "14.1727",
        "airports_countryCode": "it",
        "airports_iataCode": "NAP",
        "airports_name": "Naples",
        "airports_regionCode": "CAMPANIA"
    },
    {
        "airports_cityCode": "CUNEO",
        "airports_coordinates_latitude": "44.547",
        "airports_coordinates_longitude": "7.62322",
        "airports_countryCode": "it",
        "airports_iataCode": "CUF",
        "airports_name": "Cuneo",
        "airports_regionCode": "PIEDMONT"
    },
    {
        "airports_cityCode": "BIRMINGHAM",
        "airports_coordinates_latitude": "52.8311",
        "airports_coordinates_longitude": "-1.32806",
        "airports_countryCode": "gb",
        "airports_iataCode": "EMA",
        "airports_name": "East Midlands",
        "airports_regionCode": "EAST_MIDLANDS"
    },
    {
        "airports_cityCode": "SANTIAGO",
        "airports_coordinates_latitude": "42.8963",
        "airports_coordinates_longitude": "-8.41514",
        "airports_countryCode": "es",
        "airports_iataCode": "SCQ",
        "airports_name": "Santiago",
        "airports_regionCode": "GALICIA"
    },
    {
        "airports_cityCode": "POZNAN",
        "airports_coordinates_latitude": "52.421",
        "airports_coordinates_longitude": "16.8263",
        "airports_countryCode": "pl",
        "airports_iataCode": "POZ",
        "airports_name": "Poznan",
        "airports_regionCode": "WIELKOPOLSKA"
    },
    {
        "airports_cityCode": "OSLO",
        "airports_coordinates_latitude": "59.1867",
        "airports_coordinates_longitude": "10.2586",
        "airports_countryCode": "no",
        "airports_iataCode": "TRF",
        "airports_name": "Oslo Torp",
        "airports_regionCode": "OSLO"
    },
    {
        "airports_cityCode": "GRENOBLE",
        "airports_coordinates_latitude": "45.3629",
        "airports_coordinates_longitude": "5.32937",
        "airports_countryCode": "fr",
        "airports_iataCode": "GNB",
        "airports_name": "Grenoble",
        "airports_regionCode": "RHONE-ALPES"
    },
    {
        "airports_cityCode": "CRETE",
        "airports_coordinates_latitude": "35.5317",
        "airports_coordinates_longitude": "24.1497",
        "airports_countryCode": "gr",
        "airports_iataCode": "CHQ",
        "airports_name": "Chania",
        "airports_regionCode": "CRETE"
    },
    {
        "airports_cityCode": "LONDON",
        "airports_coordinates_latitude": "51.1481",
        "airports_coordinates_longitude": "-0.190278",
        "airports_countryCode": "gb",
        "airports_iataCode": "LGW",
        "airports_name": "London Gatwick",
        "airports_regionCode": "GREATER_LONDON"
    },
    {
        "airports_cityCode": "TALLINN",
        "airports_coordinates_latitude": "59.4133",
        "airports_coordinates_longitude": "24.8328",
        "airports_countryCode": "ee",
        "airports_iataCode": "TLL",
        "airports_name": "Tallinn",
        "airports_regionCode": "HARJU"
    },
    {
        "airports_cityCode": "LAPPEENRANTA",
        "airports_coordinates_latitude": "61.0446",
        "airports_coordinates_longitude": "28.1444",
        "airports_countryCode": "fi",
        "airports_iataCode": "LPP",
        "airports_name": "Lappeenranta",
        "airports_regionCode": "SOUTH_KARELIA"
    },
    {
        "airports_cityCode": "HAUGESUND",
        "airports_coordinates_latitude": "59.3453",
        "airports_coordinates_longitude": "5.20836",
        "airports_countryCode": "no",
        "airports_iataCode": "HAU",
        "airports_name": "Haugesund",
        "airports_regionCode": "HAUSGESUND"
    },
    {
        "airports_cityCode": "MARRAKESH",
        "airports_coordinates_latitude": "31.6069",
        "airports_coordinates_longitude": "-8.0363",
        "airports_countryCode": "ma",
        "airports_iataCode": "RAK",
        "airports_name": "Marrakesh",
        "airports_regionCode": "MARRAKESH-SAFI"
    },
    {
        "airports_cityCode": "MADRID",
        "airports_coordinates_latitude": "40.4936",
        "airports_coordinates_longitude": "-3.56676",
        "airports_countryCode": "es",
        "airports_iataCode": "MAD",
        "airports_name": "Madrid",
        "airports_regionCode": "MADRID"
    },
    {
        "airports_cityCode": "GUAYAQUIL",
        "airports_coordinates_latitude": "-2.0927",
        "airports_coordinates_longitude": "-79.5301",
        "airports_countryCode": "ec",
        "airports_iataCode": "GYE",
        "airports_name": "Guayaquil",
        "airports_regionCode": "GUAYAS"
    },
    {
        "airports_cityCode": "DERRY",
        "airports_coordinates_latitude": "55.0428",
        "airports_coordinates_longitude": "-7.16111",
        "airports_countryCode": "gb",
        "airports_iataCode": "LDY",
        "airports_name": "Derry",
        "airports_regionCode": "ULSTER"
    },
    {
        "airports_cityCode": "VALENCIA",
        "airports_coordinates_latitude": "39.999",
        "airports_coordinates_longitude": "0.026",
        "airports_countryCode": "es",
        "airports_iataCode": "CDT",
        "airports_name": "Castellon (Valencia)",
        "airports_regionCode": "COSTA_AZAHAR"
    },
    {
        "airports_cityCode": "BRATISLAVA",
        "airports_coordinates_latitude": "48.1702",
        "airports_coordinates_longitude": "17.2127",
        "airports_countryCode": "sk",
        "airports_iataCode": "BTS",
        "airports_name": "Bratislava",
        "airports_regionCode": "BRATISLAVA"
    },
    {
        "airports_cityCode": "NIMES",
        "airports_coordinates_latitude": "43.7574",
        "airports_coordinates_longitude": "4.41635",
        "airports_countryCode": "fr",
        "airports_iataCode": "FNI",
        "airports_name": "Nimes",
        "airports_regionCode": "LANGUEDOC-ROUSSILLON"
    },
    {
        "airports_cityCode": "BYDGOSZCZ",
        "airports_coordinates_latitude": "53.0968",
        "airports_coordinates_longitude": "17.9777",
        "airports_countryCode": "pl",
        "airports_iataCode": "BZG",
        "airports_name": "Bydgoszcz",
        "airports_regionCode": "KUJAWSKO-POMORSKIE"
    },
    {
        "airports_cityCode": "VERONA",
        "airports_coordinates_latitude": "45.3957",
        "airports_coordinates_longitude": "10.8885",
        "airports_countryCode": "it",
        "airports_iataCode": "VRN",
        "airports_name": "Verona",
        "airports_regionCode": "VENETO"
    },
    {
        "airports_cityCode": "TEL_AVIV",
        "airports_coordinates_latitude": "32.0034",
        "airports_coordinates_longitude": "34.5258",
        "airports_countryCode": "il",
        "airports_iataCode": "TLV",
        "airports_name": "Tel Aviv",
        "airports_regionCode": "DEFAULT_IL"
    },
    {
        "airports_cityCode": "BEZIERS",
        "airports_coordinates_latitude": "43.3235",
        "airports_coordinates_longitude": "3.3539",
        "airports_countryCode": "fr",
        "airports_iataCode": "BZR",
        "airports_name": "Beziers",
        "airports_regionCode": "LANGUEDOC-ROUSSILLON"
    },
    {
        "airports_cityCode": "SAO_PAULO",
        "airports_coordinates_latitude": "-23.2608",
        "airports_coordinates_longitude": "-46.2823",
        "airports_countryCode": "br",
        "airports_iataCode": "GRU",
        "airports_name": "Sao Paulo Guarulhos",
        "airports_regionCode": "BRAZIL_SOUTHEAST"
    },
    {
        "airports_cityCode": "PALERMO",
        "airports_coordinates_latitude": "38.176",
        "airports_coordinates_longitude": "13.091",
        "airports_countryCode": "it",
        "airports_iataCode": "PMO",
        "airports_name": "Palermo",
        "airports_regionCode": "SICILY"
    },
    {
        "airports_cityCode": "DUBLIN",
        "airports_coordinates_latitude": "53.4213",
        "airports_coordinates_longitude": "-6.27007",
        "airports_countryCode": "ie",
        "airports_iataCode": "DUB",
        "airports_name": "Dublin",
        "airports_regionCode": "LEINSTER"
    },
    {
        "airports_cityCode": "SANTANDER",
        "airports_coordinates_latitude": "43.4271",
        "airports_coordinates_longitude": "-3.82001",
        "airports_countryCode": "es",
        "airports_iataCode": "SDR",
        "airports_name": "Santander",
        "airports_regionCode": "CANTABRIA"
    },
    {
        "airports_cityCode": "CRAIOVA",
        "airports_coordinates_latitude": "44.3181",
        "airports_coordinates_longitude": "23.8886",
        "airports_countryCode": "ro",
        "airports_iataCode": "CRA",
        "airports_name": "Craiova",
        "airports_regionCode": "DEFAULT_RO"
    },
    {
        "airports_cityCode": "BOSTON",
        "airports_coordinates_latitude": "42.2147",
        "airports_coordinates_longitude": "71.0023",
        "airports_countryCode": "us",
        "airports_iataCode": "BOS",
        "airports_name": "Boston",
        "airports_regionCode": "MASSACHUSETTS"
    }
]

@app.route('/planner', methods=['GET'])
def get_planner():
    return jsonify({'route': route,"details":details})


@app.route('/cities', methods=['GET'])
def cities():
    city = request.args.getlist('name')
    return jsonify({'cities': city})

@app.route('/date/<date:dates>', methods=['GET'])
def date(dates):
	date = dates
	date = str(date)
	return jsonify({'date': date})

@app.route('/airports/all', methods=['GET'])
def get_all_airports():
    return jsonify(airports)


@app.route('/planner/startCity/<string:cityName>/startDate/<date:dates>/cities/<listofstrings:cities>/days/<listofints:days>', methods=['GET'])
def getStart(dates,cityName,cities,days):
	city = request.args.get('name')
	date = dates
	date = str(date)
	#http://localhost:5000/planner/startCity/MADRID/startDate/2017-02-03/cities/GRECE-LISBONNE/days/2-3
	return jsonify({'startDate': date,'startCity':cityName,'cities':cities,'days':days})




if __name__ == '__main__':
    app.run(debug=True)

