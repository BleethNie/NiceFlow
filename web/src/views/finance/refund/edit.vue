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
            <el-form ref="formRef" :model="formData" label-width="120px" >
                <el-form-item label="微信名称" prop="account_uid" >
                    <el-input v-model="formData.wei_xin_name" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="退单时间" prop="qian_liao_name" >
                    <el-input v-model="formData.refund_time" placeholder="请输入内容" clearable />
                </el-form-item>
                <el-form-item label="退款金额" prop="ding_ding_name" >
                    <el-input v-model="formData.refund_amount" placeholder="请输入内容" clearable />
                </el-form-item>
              
                <el-form-item label="退款账户" prop="order_amount" >
                    <el-input v-model="formData.refund_account" placeholder="请输入内容" clearable />
                </el-form-item>
            </el-form>
        </popup>
    </div>
</template>
<script lang="ts" setup>
import type { FormInstance } from 'element-plus'
import Popup from '@/components/popup/index.vue'
import { refundAdd, refundEdit } from '@/api/finance/refund'

import feedback from '@/utils/feedback'
const emit = defineEmits(['success', 'close'])
const formRef = shallowRef<FormInstance>()
const popupRef = shallowRef<InstanceType<typeof Popup>>()
const mode = ref('add')
const popupTitle = computed(() => {
    return mode.value == 'edit' ? '编辑退单记录' : '新增退单记录'
})

const formData = reactive({
    id: '',
    wei_xin_name: '',
    refund_time: '',
    refund_amount: '',
    refund_account: '',
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
    mode.value == 'edit' ? await refundEdit(formData) : await refundAdd(formData)
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
