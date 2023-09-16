from fastapi import APIRouter, Depends, Request

from like.front.schemas.article import ArticleSearchOut
from like.front.schemas.index import PolicyIn, DecorateIn, SearchIn
from like.front.service.index import IndexService, IIndexService
from like.http_base import unified_resp
from like.schema_base import PageInationResult

router = APIRouter()


@router.get('/index')
@unified_resp
async def index(index_service: IIndexService = Depends(IndexService.instance)):
    return await index_service.index()


@router.get('/decorate')
@unified_resp
async def decorate(decorate_in: DecorateIn = Depends(), index_service: IIndexService = Depends(IndexService.instance)):
    return await index_service.decorate(decorate_in.id)


@router.get('/config')
@unified_resp
async def config(request: Request, index_service: IIndexService = Depends(IndexService.instance)):
    domain = f'{request.url.hostname}:{request.url.port}' if request.url.port else request.url.hostname
    return await index_service.config(domain)


@router.get('/policy')
@unified_resp
async def policy(policy_in: PolicyIn = Depends(), index_service: IIndexService = Depends(IndexService.instance)):
    """协议"""
    return await index_service.policy(policy_in)


@router.get('/hotSearch')
@unified_resp
async def hot_search(index_service: IIndexService = Depends(IndexService.instance)):
    """热搜"""
    return await index_service.hot_search()


@router.get('/search', response_model=PageInationResult[ArticleSearchOut])
@unified_resp
async def search(search_in: SearchIn = Depends(), index_service: IIndexService = Depends(IndexService.instance)):
    """搜索"""
    return await index_service.search(search_in)
