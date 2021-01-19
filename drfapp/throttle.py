from rest_framework.throttling import SimpleRateThrottle


class MyThrottle(SimpleRateThrottle):
    scope = "send"

    # 只对含有手机号的请求做验证
    def get_cache_key(self, request, view):
        phone = request.query_params.get("phone")

        # 如果当前请求不存在手机号，则不限制
        if not phone:
            return None

        # 返回数据
        return "throttle_%(scope)s_%(ident)s" % {"scope": self.scope, "ident": phone}
