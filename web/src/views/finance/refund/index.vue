<template>
    <div class="article-lists">
        <el-card class="!border-none" shadow="never">
            <el-form ref="formRef" class="mb-[-16px]" :model="queryParams" :inline="true">
                <el-form-item label="微信名称">
                    <el-input
                        class="w-[280px]"
                        v-model="queryParams.wei_xin_name"
                        clearable
                        @keyup.enter="resetPage"
                    />
                </el-form-item>
                <el-form-item label="退单时间">
                    <daterange-picker
                        v-model:startTime="queryParams.refund_start_time"
                        v-model:endTime="queryParams.refund_end_time"
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
                    <el-button type="primary" class="mb-4"  @click="handleAdd">
                        <template #icon>
                            <icon name="el-icon-Plus" />
                        </template>
                        新增记录
                    </el-button>
                    <el-button type="success" class="mb-4" @click="handleExport">
                        <template #icon>
                          <icon name="el-icon-fold" />
                        </template>
                         导出记录
                    </el-button>
            </div>
            <el-table size="large" v-loading="pager.loading" :data="pager.lists">
                <el-table-column label="ID" prop="id" min-width="80" />
                <el-table-column label="微信名称" prop="wei_xin_name" min-width="120" />
                <el-table-column label="退单时间" prop="refund_time" min-width="120" />
                <el-table-column label="退款金额" prop="refund_amount" min-width="120" />
                <el-table-column label="退款账户" prop="refund_account" min-width="120" />

                <el-table-column label="操作" width="120" fixed="right">
                    <template #default="{ row }">
                        <el-button type="primary" link @click="handleEdit(row)">
                                编辑
                        </el-button>
                        <el-button
                            type="danger"
                            link
                            @click="handleDelete(row.id)"
                        >
                            删除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="flex justify-end mt-4">
                <pagination v-model="pager" @change="getLists" />
            </div>
        </el-card>
        <edit-popup v-if="showEdit" ref="editRef" @success="getLists" @close="showEdit = false"/>

    </div>
</template>
<script lang="ts" setup name="refundLists">
import {refundDelete, refundExport, refundList} from '@/api/finance/refund'
import {usePaging} from '@/hooks/usePaging'
import feedback from '@/utils/feedback'
import EditPopup from "@/views/finance/refund/edit.vue";
import moment from "moment/moment";
import {streamFileDownload} from "@/utils/file";

const editRef = shallowRef<InstanceType<typeof EditPopup>>();
const showEdit = ref(false);

const queryParams = reactive({
    wei_xin_name: '',
    refund_start_time: '',
    refund_end_time: ''
})

const { pager, getLists, resetPage, resetParams } = usePaging({
    fetchFun: refundList,
    params: queryParams
})

const handleAdd = async () => {
    showEdit.value = true;
    await nextTick();
    editRef.value?.open("add");
}

const handleEdit = async (data: any) => {
    showEdit.value = true;
    await nextTick();
    editRef.value?.open("edit");
    editRef.value?.setFormData(data);
}

const handleExport =  async () => {
    const file = await refundExport()
    console.log(file)
    const date_format = moment().format("YYYYMMDD_HHmmss")
    const file_name = "refund_"+date_format+".xlsx"
    streamFileDownload(file, file_name)
}

const handleDelete = async (id: number) => {
    await feedback.confirm('确定要删除？')
    await refundDelete({ id })
    feedback.msgSuccess('删除成功')
    getLists()
}

onActivated(() => {
    getLists()
})

getLists()
</script>
