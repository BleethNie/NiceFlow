import request from '@/utils/request'


// 退单列表
export function refundList(params?: any) {
    return request.get({ url: '/finance/refund/list', params })
}
//退单列表
export function refundAll(params?: any) {
    return request.get({ url: '/finance/refund/all', params })
}

// 添加退单
export function refundAdd(params: any) {
    return request.post({ url: '/finance/refund/add', params })
}

// 编辑退单
export function refundEdit(params: any) {
    return request.post({ url: '/finance/refund/edit', params })
}

// 删除退单
export function refundDelete(params: any) {
    return request.post({ url: '/finance/refund/del', params })
}

//退单详情
export function refundDetail(params: any) {
    return request.get({ url: '/finance/refund/detail', params })
}

export function refundExport() {
    return request.get({
        url: "/finance/refund/export",
        responseType: 'blob'
    }, {
        isTransformResponse: false
    })
}
