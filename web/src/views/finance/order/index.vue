<template>
    <div class="article-lists">
        <el-card class="!border-none" shadow="never">
            <el-form ref="formRef" class="mb-[-16px]" :model="queryParams" :inline="true">
                <el-form-item label="钉钉群">
                    <el-input
                            class="w-[280px]"
                            v-model="queryParams.ding_ding_group"
                            clearable
                            @keyup.enter="resetPage"
                    />
                </el-form-item>
                <el-form-item label="订单时间">
                    <daterange-picker
                            type="datetimerange"
                            v-model:startTime="queryParams.order_start_time"
                            v-model:endTime="queryParams.order_end_time"
                    />
                </el-form-item>

                <el-form-item label="购买平台">
                    <el-input
                            class="w-[280px]"
                            v-model="queryParams.order_platform"
                            clearable
                            @keyup.enter="resetPage"
                    />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="resetPage">查询</el-button>
                    <el-button @click="resetParams">重置</el-button>
                </el-form-item>
            </el-form>
        </el-card>
        <el-card class="!border-none mt-4" shadow="never">
            <div>
                <el-button type="primary" class="mb-4" @click="handleAdd">
                    <template #icon>
                        <icon name="el-icon-Plus"/>
                    </template>
                    新增记录
                </el-button>
                <el-button type="success" class="mb-4" @click="handleExport">
                    <template #icon>
                        <icon name="el-icon-fold"/>
                    </template>
                    导出记录
                </el-button>
            </div>
            <el-table size="large" v-loading="pager.loading" :data="pager.lists">

                <el-table-column label="ID" prop="id" min-width="80"/>
                <el-table-column label="用户ID" prop="account_uid" min-width="100"/>
                <el-table-column label="千聊名称" prop="qian_liao_name" min-width="100"/>
                <el-table-column label="钉钉名称" prop="ding_ding_name" min-width="100"/>
                <el-table-column label="微信名称" prop="wei_xin_name" min-width="100"/>
                <el-table-column label="头条名称" prop="tou_tiao_name" min-width="100"/>
                <el-table-column label="钉钉群" prop="ding_ding_group" min-width="100"/>
                <el-table-column label="手机号" prop="phone_num" min-width="120"/>
                <el-table-column label="订单时间" prop="order_time" min-width="100"/>
                <el-table-column label="交易内容" prop="order_content" min-width="100"/>
                <el-table-column label="购买平台" prop="order_platform" min-width="120"/>
                <el-table-column label="交易类型" prop="order_type" min-width="100"/>
                <el-table-column label="支付金额（元）" prop="order_amount" min-width="130"/>
                <el-table-column label="订单来源" prop="order_source" min-width="100"/>
                <el-table-column label="收益金额（元）" prop="income_amount" min-width="130"/>
                <el-table-column label="促销类型" prop="promotion_type" min-width="100"/>
                <el-table-column label="优惠券类型" prop="coupon_type" min-width="120"/>
                <el-table-column label="优惠券" prop="coupon" min-width="100"/>

                <el-table-column label="操作" width="120" fixed="right">
                    <template #default="{ row }">
                        <el-button type="primary" link @click="handleEdit(row)">
                            编辑
                        </el-button>
                        <el-button  type="danger" link @click="handleDelete(row.id)">
                            删除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="flex justify-end mt-4">
                <pagination v-model="pager" @change="getLists"/>
            </div>
        </el-card>
        <edit-popup v-if="showEdit" ref="editRef" @success="getLists" @close="showEdit = false"/>
    </div>
</template>
<script lang="ts" setup name="orderLists">
import {orderDelete, orderExport, orderList} from "@/api/finance/order";
import {usePaging} from "@/hooks/usePaging";
import feedback from "@/utils/feedback";
import EditPopup from "@/views/finance/order/edit.vue";
import {streamFileDownload} from "@/utils/file";
import moment from 'moment';

const editRef = shallowRef<InstanceType<typeof EditPopup>>();
const showEdit = ref(false);

const queryParams = reactive({
    ding_ding_group: "",
    order_start_time: "",
    order_end_time: "",
    order_platform: ""
});

const {pager, getLists, resetPage, resetParams} = usePaging({
    fetchFun: orderList,
    params: queryParams
});


const handleAdd = async () => {
    showEdit.value = true;
    await nextTick();
    editRef.value?.open("add");
};

const handleExport =  async () => {
    const file = await orderExport()
    console.log(file)
    const date_format = moment().format("YYYYMMDD_HHmmss")

    const file_name = "order_"+date_format+".xlsx"
    streamFileDownload(file, file_name)
}



const handleEdit = async (data: any) => {
    showEdit.value = true;
    await nextTick();
    editRef.value?.open("edit");
    editRef.value?.setFormData(data);
};

const handleDelete = async (id: number) => {
    await feedback.confirm("确定要删除？");
    await orderDelete({id});
    feedback.msgSuccess("删除成功");
    getLists();
};

onActivated(() => {
    getLists();
});

getLists();
</script>
