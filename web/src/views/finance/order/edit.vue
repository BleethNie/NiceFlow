<template>
    <div class="edit-popup">
        <popup
            ref="popupRef"
            :title="popupTitle"
            :async="true"
            width="650px"
            @confirm="handleSubmit"
            @close="handleClose"
        >
            <el-form ref="formRef" :model="formData" label-width="84px" >
                <el-form-item label="用户ID" prop="account_uid" label-width="120">
                    <el-input v-model="formData.account_uid" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="千聊名称" prop="qian_liao_name" label-width="120">
                    <el-input v-model="formData.qian_liao_name" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="钉钉名称" prop="ding_ding_name" label-width="120">
                    <el-input v-model="formData.ding_ding_name" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="微信名称" prop="wei_xin_name" label-width="120">
                    <el-input v-model="formData.wei_xin_name" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="头条名称" prop="tou_tiao_name" label-width="120">
                    <el-input v-model="formData.tou_tiao_name" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="钉钉群" prop="ding_ding_group" label-width="120">
                    <el-input v-model="formData.ding_ding_group" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="手机号" prop="phone_num" label-width="120">
                    <el-input v-model="formData.phone_num" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="订单时间" prop="order_time" label-width="120">
                    <el-input v-model="formData.order_time" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="交易内容" prop="order_content" label-width="120">
                    <el-input v-model="formData.order_content" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="购买平台" prop="order_platform" label-width="120">
                    <el-input v-model="formData.order_platform" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="交易类型" prop="order_type" label-width="120">
                    <el-input v-model="formData.order_type" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="促销类型" prop="promotion_type" label-width="120">
                    <el-input v-model="formData.promotion_type" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="优惠券类型" prop="coupon_type" label-width="120">
                    <el-input v-model="formData.coupon_type" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="优惠券" prop="coupon" label-width="120">
                    <el-input v-model="formData.coupon" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="支付金额(元)" prop="order_amount" label-width="120">
                    <el-input v-model="formData.order_amount" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="订单来源" prop="order_source" label-width="120">
                    <el-input v-model="formData.order_source" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="收益金额(元)" prop="income_amount" label-width="120">
                    <el-input v-model="formData.income_amount" placeholder="请输入内容" clearable />
                </el-form-item>
            </el-form>
        </popup>
    </div>
</template>
<script lang="ts" setup>
import type { FormInstance } from 'element-plus'
import Popup from '@/components/popup/index.vue'
import { orderAdd, orderEdit } from '@/api/finance/order'
import { uuid  } from 'vue3-uuid';

import feedback from '@/utils/feedback'
import moment from "moment/moment";
const emit = defineEmits(['success', 'close'])
const formRef = shallowRef<FormInstance>()
const popupRef = shallowRef<InstanceType<typeof Popup>>()
const mode = ref('add')
const popupTitle = computed(() => {
    return mode.value == 'edit' ? '编辑订单记录' : '新增订单记录'
})

const formData = reactive({
    id: '',
    account_uid: uuid.v1(),
    qian_liao_name: '天机短线交流群泽恩小弟',
    ding_ding_name: '',
    wei_xin_name: '',
    tou_tiao_name: '',
    phone_num: '',
    order_time: moment().format("YYYY-MM-DD HH:mm:ss"),
    order_content: '',
    order_platform: '今日头条',
    order_type: '',
    promotion_type: '',
    coupon_type: '',
    coupon: '',
    order_amount: '275',
    order_source: '',
    income_amount: '',
    ding_ding_group: '',
})

const setFormData = (data: Record<any, any>) => {
    for (const key in formData) {
        if (data[key] != null && data[key] != undefined) {
            //@ts-ignore
            formData[key] = data[key]
        }
    }
}


const handleSubmit = async () => {
    await formRef.value?.validate()
    mode.value == 'edit' ? await orderEdit(formData) : await orderAdd(formData)
    popupRef.value?.close()
    feedback.msgSuccess('操作成功')
    emit('success')
}

const open = (type = 'add') => {
    mode.value = type
    popupRef.value?.open()
}


const handleClose = () => {
    emit('close')
}

defineExpose({
    open,
    setFormData
})
</script>
