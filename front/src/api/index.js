import client from "./client";

export default {
    async login(username, password) {
        const { data } = await client.post('/api-token-auth/', { username, password });
        localStorage.setItem('token', data.token);
        return data.token;
    },

    async logout() {
        localStorage.removeItem('token');
    },

    async uploadFile(file) {
        const formData = new FormData();
        formData.append('file', file, file.filename);
        const { data } = await client.post('/administration/api/files/', formData, { headers: { 'Content-Type': 'multipart/form-data' } });
        return data;
    },

    async listTextures() {
        const {data} = await client.get('/administration/api/texture/');
        return data;
    },

    async createTexture(file_id) {
        const {data} = await client.post('/administration/api/texture/', { file: file_id });
        return data;
    },

    async deleteTexture(id) {
        const {data} = await client.delete(`/administration/api/texture/${id}/`);
        return data;
    },

    async listObjects() {
        const {data} = await client.get(`/administration/api/object/`);
        return data;
    },

    async getObject(id) {
        const {data} = await client.get(`/administration/api/object/${id}/`);
        return data;
    },

    async createObject(preview_file_id, object_file_id, files_ids) {
        const {data} =  await client.post(`/administration/api/object/`, {
            file: object_file_id,
            preview: preview_file_id,
            textures: files_ids,
        });

        return data;
    },

    async deleteObject(id) {
        const {data} = await client.delete(`/administration/api/object/${id}/`);
        return data;
    },

    async updateObject(id, preview_file_id, object_file_id, files_ids) {
        const {data} =  await client.put(`/administration/api/object/${id}/`, {
            file: object_file_id,
            preview: preview_file_id,
            textures: files_ids,
        });

        return data;
    }
}