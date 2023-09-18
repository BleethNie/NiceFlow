import { ref } from 'vue'
import feedback from '@/utils/feedback'
import type { FormRules } from 'element-plus'
import { setOaMenuSave, getOaMenu, setOaMenuPublish } from '@/api/channel/wx_oa'
import type { Menu } from '@/api/channel/wx_oa'

// 菜单实例
export const menuRef = shallowRef()
// 菜单数据
const menuList = ref<Menu[]>([])
const menuIndex = ref<number>(0)

// 校验
export const rules = reactive<FormRules>({
    name: [
        {
            required: true,
            message: '必填项不能为空',
            trigger: ['blur', 'change']
        },
        {
            min: 1,
            max: 12,
            message: '长度限制12个字符',
            trigger: ['blur', 'change']
        }
    ],
    menuType: [
        {
            required: true,
            message: '必填项不能为空',
            trigger: ['blur', 'change']
        }
    ],
    visitType: [
        {
            required: true,
            message: '必填项不能为空',
            trigger: ['blur', 'change']
        }
    ],
    url: [
        {
            required: true,
            message: '必填项不能为空',
            trigger: ['blur', 'change']
        },
        {
            pattern:
                /^([hH][tT]{2}[pP]:\/\/|[hH][tT]{2}[pP][sS]:\/\/)(([A-Za-z0-9-~]+)\.)+([A-Za-z0-9-~\/])+$/,
            message: '请输入合法的网址链接',
            trigger: ['blur', 'change']
        }
    ],
    appId: [
        {
            required: true,
            message: '必填项不能为空',
            trigger: ['blur', 'change']
        }
    ],
    pagePath: [
        {
            required: true,
            message: '必填项不能为空',
            trigger: ['blur', 'change']
        }
    ]
})

export const useMenuOa = (ref: any) => {
    if (ref) menuRef.value = ref

    // 添加主菜单
    const handleAddMenu = () => {
        menuList.value.push({
            name: '菜单名称',
            menuType: 1,
            visitType: 'view',
            url: '',
            appId: '',
            pagePath: '',
            subButtons: []
        })
    }

    // 添加子菜单
    const handleAddSubMenu = (event?: Menu) => {
        const index = menuIndex.value
        if (menuList.value[index].subButtons.length >= 5) {
            feedback.msgError('已添加上限～')
            return
        }
        menuList.value[index].subButtons.push(event)
    }

    // 编辑子菜单
    const handleEditSubMenu = (event: Menu, subIndex: number) => {
        const index = menuIndex.value
        menuList.value[index].subButtons[subIndex] = event
    }

    // 删除主菜单
    const handleDelMenu = (index: number) => {
        menuList.value.splice(index, 1)
    }

    // 删除子菜单
    const handleDelSubMenu = (index: number, subIndex: number) => {
        menuList.value[index].subButtons.splice(subIndex, 1)
    }

    // 获取菜单
    const getOaMenuFunc = async () => {
        try {
            menuList.value = await getOaMenu()
        } catch (error) {
            console.log('获取菜单=>', error)
        }
    }

    // 保存菜单
    const handleSave = async () => {
        const refs = menuRef.value.value
        for (let i = 0; i < refs.length; i++) {
            try {
                await refs[i].menuFormRef.validate()
            } catch (error) {
                menuIndex.value = i
                return
            }
        }
        await setOaMenuSave(menuList.value)
        feedback.msgSuccess('保存成功')
    }

    // 保存菜单
    const handlePublish = async () => {
        const refs = menuRef.value.value
        for (let i = 0; i < refs.length; i++) {
            try {
                await refs[i].menuFormRef.validate()
            } catch (error) {
                menuIndex.value = i
                return
            }
        }
        await setOaMenuPublish(menuList.value)
        feedback.msgSuccess('发布成功')
    }

    return {
        menuList,
        menuIndex,
        handleAddMenu,
        handleAddSubMenu,
        handleEditSubMenu,
        handleDelMenu,
        handleDelSubMenu,
        getOaMenuFunc,
        handleSave,
        handlePublish
    }
}
