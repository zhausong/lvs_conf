#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys

import template


def main():
    template_dir = "./template"
    template_dest_dir = "/tmp/lvs/"

    device = "p1p2"

    vipnets = [
        "10.0.12.0/24"
    ]

    vip2ws = [
        {
            'wstype': 'apps', 
            'vip': '10.0.12.201', 
            'wss': ['apps-intngtest0-bgp0.hy01'], 
            'ports': [
                {'dport': 80, 'synproxy': 1, 'sport': 80, 'persistence_timeout': 50}, 
                {'dport': 443, 'synproxy': 1, 'sport': 443, 'persistence_timeout': 50}
            ]
        },
        {
            'wstype': 'search', 
            'vip': '10.0.12.202', 
            'wss': ['search-intngtest0-bgp0.hy01'], 
            'ports': [
                {'dport': 80, 'synproxy': 1, 'sport': 80, 'persistence_timeout': 50}, 
                {'dport': 443, 'synproxy': 1, 'sport': 443, 'persistence_timeout': 50}
            ]
        }
    ]

    lb_infos = [
        {
            "internalgateway": "10.0.18.1",
            "internalnetmask": "255.255.255.224",
            "hostname": "sa-intlb0-bgp0.hy01",
            "routerid": "10.0.18.2",
            "internalip": "10.0.18.2",
            "ospfnet": "10.0.18.0/27",
            "localips": [
                '10.0.18.3', 
                '10.0.18.4', 
                '10.0.18.5', 
                '10.0.18.6', 
                '10.0.18.7', 
                '10.0.18.8', 
                '10.0.18.9', 
                '10.0.18.10', 
                '10.0.18.11', 
                '10.0.18.12', 
                '10.0.18.13', 
                '10.0.18.14', 
                '10.0.18.15', 
                '10.0.18.16', 
                '10.0.18.17', 
                '10.0.18.18', 
                '10.0.18.19', 
                '10.0.18.20', 
                '10.0.18.21', 
                '10.0.18.22', 
                '10.0.18.23', 
                '10.0.18.24', 
                '10.0.18.25', 
                '10.0.18.26', 
                '10.0.18.27', 
                '10.0.18.28', 
                '10.0.18.29', 
                '10.0.18.30'
            ]
        },
        {
            "internalgateway": "10.0.18.33",
            "internalnetmask": "255.255.255.224",
            "hostname": "sa-intlb1-bgp0.hy01",
            "routerid": "10.0.18.34",
            "internalip": "10.0.18.34",
            "ospfnet": "10.0.18.32/27",
            "localips": [
                '10.0.18.35',
                '10.0.18.36',
                '10.0.18.37',
                '10.0.18.38',
                '10.0.18.39',
                '10.0.18.40',
                '10.0.18.41',
                '10.0.18.42',
                '10.0.18.43',
                '10.0.18.44',
                '10.0.18.45',
                '10.0.18.46',
                '10.0.18.47',
                '10.0.18.48',
                '10.0.18.49',
                '10.0.18.50',
                '10.0.18.51',
                '10.0.18.52',
                '10.0.18.53',
                '10.0.18.54',
                '10.0.18.55',
                '10.0.18.56',
                '10.0.18.57',
                '10.0.18.58',
                '10.0.18.59',
                '10.0.18.60',
                '10.0.18.61',
                '10.0.18.62',
            ]
        }
    ]

    print template.get(template_dir, template_dest_dir, \
        device, vipnets, vip2ws, lb_infos)


if __name__ == '__main__':
    main()
