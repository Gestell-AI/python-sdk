import pytest
from gestell import Gestell

gestell = Gestell(key='INVALID KEY', debug=True)


@pytest.mark.asyncio
async def test_organization_get_error():
    response = await gestell.organization.get('...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_organization_list_error():
    response = await gestell.organization.list()
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_organization_update_error():
    response = await gestell.organization.update(
        id='...', name='...', description='...'
    )
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_organization_create_error():
    response = await gestell.organization.create(name='...', description='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_organization_add_members_error():
    response = await gestell.organization.addMembers(id='...', members=[])
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_organization_remove_members_error():
    response = await gestell.organization.removeMembers(id='...', members=[])
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_organization_delete_error():
    response = await gestell.organization.delete('...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_get_error():
    response = await gestell.collection.get('...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_list_error():
    response = await gestell.collection.list()
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_create_error():
    response = await gestell.collection.create(
        organizationId='...', name='...', description='...', type='canon'
    )
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_update_error():
    response = await gestell.collection.update(collection_id='...', name='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_delete_error():
    response = await gestell.collection.delete('...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_query_search_error():
    response = await gestell.query.search(collection_id='...', prompt='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_query_prompt_error():
    response = gestell.query.prompt(collection_id='...', prompt='...')
    full_response = b''
    async for chunk in response:
        full_response += chunk

    result = full_response.decode('utf-8')
    assert len(result) > 1


@pytest.mark.asyncio
async def test_collection_query_table_error():
    response = await gestell.query.table(collection_id='...', category_id='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_query_features_error():
    response = await gestell.query.features(collection_id='...', category_id='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_job_get_error():
    response = await gestell.job.get(collection_id='...', job_id='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_job_list_error():
    response = await gestell.job.list(collection_id='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_job_reprocess_error():
    response = await gestell.job.reprocess(collection_id='...', type='status', ids=[])
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_job_cancel_error():
    response = await gestell.job.cancel(collection_id='...', ids=[])
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_document_get_error():
    response = await gestell.document.get(collection_id='...', document_id='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_document_list_error():
    response = await gestell.document.list(collection_id='...')
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_document_presign_error():
    response = await gestell.document.presign(
        collection_id='...', type='...', filename='...'
    )
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_document_create_error():
    response = await gestell.document.create(
        collection_id='...', type='...', name='...', path='...'
    )
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_document_update_error():
    response = await gestell.document.update(
        collection_id='...', document_id='...', name='...'
    )
    assert response.status == 'ERROR'


@pytest.mark.asyncio
async def test_collection_document_delete_error():
    response = await gestell.document.delete(collection_id='...', document_id='...')
    assert response.status == 'ERROR'