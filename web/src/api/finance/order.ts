import request from "@/utils/request";


// 订单列表
export function orderList(params?: any) {
    return request.get({url: "/finance/order/list", params});
}

// 订单列表
export function orderAll(params?: any) {
    return request.get({url: "/finance/order/all", params});
}

// 添加订单
export function orderAdd(params: any) {
    return request.post({url: "/finance/order/add", params});
}

// 编辑订单
export function orderEdit(params: any) {
    return request.post({url: "/finance/order/edit", params});
}

// 导出订单
export function orderExport() {
    return request.get({
        url: "/finance/order/export",
        responseType: 'blob'
    }, {
        isTransformResponse: false
    })
}


// 删除订单
export function orderDelete(params: any) {
    return request.post({url: "/finance/order/del", params});
}

//订单详情
export function orderDetail(params: any) {
    return request.get({url: "/finance/order/detail", params});
}

