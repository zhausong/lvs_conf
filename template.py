#-*- coding: utf-8 -*-

"""
    生成 lvs 配置文件.

"""

import os

from jinja2 import Environment, FileSystemLoader


def get(template_dir, template_dest_dir, device, vipnets, vip2ws, lb_infos):
    """ 生成 lvs 配置文件.

    """
    if not os.path.exists(template_dest_dir):
        os.mkdir(template_dest_dir)

    # 模板名称.
    keepalived_template = "keepalived.conf"
    sub_keepalived_template = "sub_keepalived.conf"
    zebra_template = "zebra.conf"
    ospfd_template = "ospfd.conf"

    # 拿到 vip 列表.
    vips = [ i["vip"] for i in vip2ws ]

    for lb_info in lb_infos:
        # 拿到 lb 信息.
        lb = lb_info["hostname"]
        internalip = lb_info["internalip"]
        internalnetmask = lb_info["internalnetmask"]
        internalgateway = lb_info["internalgateway"]
        routerid = lb_info["routerid"]
        ospfnet = lb_info["ospfnet"]
        localips = lb_info["localips"]

        # lb 配置文件基目录.
        lb_dir = template_dest_dir + "/" + lb
        os.mkdir(lb_dir)

        # keepalived 配置文件目录.
        lb_keepalived_dir = lb_dir + "/keepalived"
        os.mkdir(lb_keepalived_dir)

        # ospfd 配置文件目录.
        lb_osfpd_dir = lb_dir + "/ospfd"
        os.mkdir(lb_osfpd_dir)

        # 模板环境.
        j2_env = Environment(loader=FileSystemLoader(template_dir),
                             trim_blocks=True)

        # 生成主 keepalived 配置文件.
        ret = j2_env.get_template(keepalived_template).render(
            lips=localips,
            vips=vips,
            lb=lb.split(".")[0]
        )
        with file(lb_keepalived_dir + "/keepalived.conf", 'w') as f:
            f.writelines(ret)

        # 生成 zebra 配置文件.
        ret = j2_env.get_template(zebra_template).render(
            lb=lb
        )
        with file(lb_osfpd_dir + "/zebra.conf", 'w') as f:
            f.writelines(ret)

        # 生成 ospfd 配置文件.
        ret = j2_env.get_template(ospfd_template).render(
            lb=lb,
            routerid=routerid, 
            device=device, 
            ospfnet=ospfnet, 
            vipnets=vipnets

        )
        with file(lb_osfpd_dir + "/ospfd.conf", 'w') as f:
            f.writelines(ret)

        # 生成 keepalived 的 VIP 配置文件.
        for i in vip2ws:
            # vip 信息.
            vip = i["vip"]

            # port 信息.
            if "ports" not in i:
                ports = [
                    {"sport": 80,
                     "dport": 80,
                     "synproxy": 1,
                     "persistence_timeout": 50
                     },
                    {"sport": 443,
                     "dport": 443,
                     "synproxy": 1,
                     "persistence_timeout": 50
                     }
                ]
            else:
                ports = list()
                for j in i["ports"]:
                    if "synproxy" not in j:
                        j["synproxy"] = 1
                    elif "persistence_timeout" not in j:
                        j["persistence_timeout"] = 50
                    ports.append(j)

            # 后端机器列表.
            wss = i["wss"]
            # wss_ips = dns_resolv(wss) #   在线上的时候需要解析成 IP, 此处暂时注释.
    
            ret = j2_env.get_template(sub_keepalived_template).render(
                vip=vip, 
                ports=ports, 
                # wss=wss_ips
                wss=wss
            )
            with file(lb_keepalived_dir + "/" + vip + ".conf", 'w') as f:
                f.writelines(ret)
