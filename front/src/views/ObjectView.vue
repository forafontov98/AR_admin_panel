<template>
  <div class="object-view">
      <div class="object-view__container">
          <div class="object-view__preview">
            <h2>Превью</h2>
            <img :src="preview.file">
            <upload-button @file-uploaded="preview = $event"/>
          </div>
          <div class="object-view__object">
              <h2>Объект</h2>
              <div class="file-uploader">
                  <div class="file-uploader__preview_text">{{ filename }}</div>
                  <upload-button @file-uploaded="object = $event"/>
              </div>
          </div>
      </div>
        <div class="object-view__textures">
            <h2>Текстуры</h2>
            <upload-button @file-uploaded="textures.push($event)"/>
            <div class="multiimage-preview">
                <div v-for="(texture, index) in textures" :key="texture.id" class="multiimage-preview__wrapper">
                  <img :src="texture.file" class="multiimage-preview__preview">
                  <img 
                    :src="require('@/assets/remove.png')"
                    class="multiimage-preview__button"
                    @click="textures.splice(index, 1)"
                  >
                </div>
            </div>
        </div>
      <base-button @click="saveObject">Сохранить</base-button>
  </div>
</template>

<script>
import API from "@/api";
import BaseButton from '@/components/BaseButton';
import UploadButton from '@/components/UploadButton';

export default {
    components: {BaseButton, UploadButton},
    props: {
        id: String,
    },
    async mounted() {
        if (this.id) {
            const {preview, textures, file} = await API.getObject(+this.id);

            this.preview = preview;
            this.object = file;
            this.textures = textures;
        }
    },
    data() {
        return {
            preview: {
                id: null,
                file: '',
            },
            textures: [],
            object: {
                id: null,
                file: '',
            }
        }
    },
    computed: {
        filename() {
            if (this.object.file) {
                return this.object.file.split('/').slice(-1)[0];
            }
            return 'Пусто'
        },
    },
    methods: {
        async saveObject() {
            const previewId = this.preview.id;
            const texturesIds = this.textures.map(i => i.id);
            const objectId = this.object.id;

            if (this.id) {
                await API.updateObject(+this.id, previewId, objectId, texturesIds);
            } else {
                await API.createObject(previewId, objectId, texturesIds);
            }

            this.$router.back();
        }
    }
}
</script>

<style>
    .object-view__container {
        display: flex;
        flex-direction: row;
        width: 100%;
    }

    .object-view__preview {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .object-view__preview img {
        width: 140px;
        height: 140px;
        border-radius: 10px;
    }

    .object-view__object {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        align-items: flex-start;
        margin-left: 50px;
    }

    .object-view__textures {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 20px;
    }

    .multiimage-preview {
        display: flex;
        flex-direction: row;
    }

    .multiimage-preview__wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-right: 10px;
    }

    .multiimage-preview__preview {
        width: 60px;
        height: 60px;
        border-radius: 10px;
    }

    .multiimage-preview__button {
        margin: 10px 0;
        width: 20px;
        height: 20px;
    }

    .file-uploader {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border: 1px dashed #C8C8C8;
        border-radius: 10px;
        background-color: #F8F8F8;
    }
</style>