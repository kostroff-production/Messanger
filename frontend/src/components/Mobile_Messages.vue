<template>
    <div class="chat-body">
        <div class="FormDiv" id="AddPhotos" style="display: none">
            <form class="FormAlbum" action="#" method="post" enctype="multipart/form-data">
                <div>
                    <svg @click="cancelForm" width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                      <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                    </svg>
                </div>
                <h3>Добавить фото</h3>
                <input class="input-file" type="file" name="photo_message" accept="image/*" required="" id="id_photo_message">
                <p id="id_photo_message_p"></p>
                <label for="id_photo_message">
                    <span class="input-label">Выберите файл</span>
                </label>
                <button class="button-FormDiv" id="btn-photo">Добавить</button>
            </form>
        </div>
        <div class="FormDiv" id="AddVideo" style="display: none">
            <form class="FormVideo" action="#" method="post" enctype="multipart/form-data">
                <div>
                    <svg @click="cancelForm" width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                      <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                    </svg>
                </div>
                <h3>Загрузка видеоконтента</h3>
                <input class="input-file" type="file" name="video" id="id_video">
                <p id="id_video_p"></p>
                <label for="id_video">
                    <span class="input-label">Выберите файл</span>
                </label>
                <button class="button-FormDiv" id="btn-video">Загрузить</button>
            </form>
        </div>
        <div id="backgroundDivForm" style="display: none"></div>
        <div id="loading-photo">
            <h3>Загружаю фото...</h3>
        </div>
        <div id="loading-video">
            <h3>Загружаю видео...</h3>
        </div>

        <BlockTopChat
            v-bind:ws-chat="wsChat"
            v-bind:slice-t-x-t-members="sliceTXTMembers"
        />

        <Messages
            v-bind:url-photo="urlPhoto"
            v-bind:person="person"
            v-bind:ws-messages="wsMessages"
            v-bind:change_chat="m_change_chat"
            @deactivateChangeChat="m_change_chat=$event"
        />

        <MessageForm
            v-bind:mobile="mobile"
            v-bind:ws-chat="wsChat"
            v-bind:url-server="urlServer"
            v-bind:url-photo="urlPhoto"
            @FormInputPhoto="AddPhotos=$event"
            @FormInputVideo="VideoForm=$event"
            @backgroundDiv="backgroundDivForm=$event"
            @funcHideSave="hideSave=$event"
            @funcCreateMessage="CreateMessage=$event"
            v-bind:trigger-w-s="triggerWS"
            @outWsMF="outWsMF"
            @fun_click="fun_click"
        />

        <div id="block-emoji" class="block-emoji">
            <Emoji
                v-bind:mobile="mobile"
            />
        </div>
    </div>
</template>

<script>
    import BlockTopChat from "./BlockTopChat";
    import Messages from "./Messages";
    import MessageForm from "./MessageForm";
    import Emoji from "./Emoji";

    export default {
        name: "Mobile_Messages",
        props: {
            cancelForm: Function,
            sliceTXTMembers: Function,
            wsChat: WebSocket,
            person: Object,
            urlPhoto: String,
            wsMessages: WebSocket,
            urlServer: String,
            mobile: Boolean,
            change_chat: Boolean,
            triggerWS: Boolean
        },
        emits: ['deactivateChangeChat', 'FormInputPhoto', 'FormInputVideo',
            'backgroundDiv', 'funcHideSave', 'funcCreateMessage', 'outWsMF',
            'fun_click'
        ],
        data() {
            return {
                wsPhotoMessage: null,
                wsVideo: null,
                AddPhotos: null,
                VideoForm: null,
                backgroundDivForm: null,
                hideSave: null,
                CreateMessage: null,
                m_change_chat: false,
                toggleAddMenu: null,
                showFormAddPhoto: null,
                showFormAddVideo: null,
                gallery: null
            }
        },
        components: { BlockTopChat, Messages, MessageForm, Emoji },
        mounted() {
            this.$emit('FormInputPhoto', this.AddPhotos);
            this.$emit('FormInputVideo', this.VideoForm);
            this.$emit('backgroundDiv', this.backgroundDivForm);
            this.$emit('funcHideSave', this.hideSave);
            this.$emit('funcCreateMessage', this.CreateMessage);
        },
        updated() {
            if (this.change_chat) {
                this.m_change_chat = true;
                this.$emit('deactivateChangeChat', false);
            }
        },
        methods: {
            outWsMF (data) {
                this.wsPhotoMessage = data.wsPhotoMessage;
                this.wsVideo = data.wsVideo;

                this.$emit('outWsMF', data);
            },
            fun_click (data) {
                var data_click = {
                    toggleAddMenu: this.toggleAddMenu = data.toggleAddMenu,
                    showFormAddPhoto: this.showFormAddPhoto = data.showFormAddPhoto,
                    showFormAddVideo: this.showFormAddVideo = data.showFormAddVideo,
                    gallery: this.gallery = data.gallery
                };
                this.$emit('fun_click', data_click);
            }
        }
    }
</script>

<style scoped>

</style>
