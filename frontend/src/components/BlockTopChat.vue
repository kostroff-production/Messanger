<template>
    <div>
        <div class="info-chat">
            <div class="chat-avatar">
                <img :src="urlPhoto + '/static/default_avatar.jpg'" alt="" class="img-circle avatar-chat">
            </div>
            <div class="chat-name">
                <p>First chat</p>
            </div>
            <div class="change-chat-name">
                <input type="text" class="change-name" value="">
            </div>
            <div class="btn-change-chat-name">
                <div class="pencil" @click="ChangeNameChat">
                    <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-pencil-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456l-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                      <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                    </svg>
                </div>
                <div class="save" @click="SaveNewNameChat">
                    <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-check2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
                    </svg>
                </div>
            </div>
            <div class="chat-btn" id="btn-info-chat">
                <svg width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-info-square-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm8.93 4.588l-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM8 5.5a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                </svg>
            </div>
        </div>

        <div class="media-files-chat-body" style="display: none">
            <div class="media-files-chat">
                <div class="med-2">
                    <label class="med-label" for="med2-1">Фото</label>
                    <input id="med2-1" name="meds-two" type="radio" checked="checked">
                    <div>
                        <div class="media_content_div active-grid" id="med-1"></div>
                        <div class="media-info-chat active-grid" id="photo-media">
                            <div class="media-content gallery-item">
                                <img class="media" :src="urlPhoto + '/static/default_avatar.jpg'" alt="">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="med-2">
                    <label class="med-label" for="med2-2">Видео</label>
                    <input id="med2-2" name="meds-two" type="radio">
                    <div>
                        <div class="media_content_div" id="med-2"></div>
                        <div class="media-info-chat" id="video-media">
                            <div class="media-content">
                                <video controls class="media">
                                    <source :src="urlPhoto + '/static/default_avatar.jpg'" type="video/mp4">
                                </video>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "BlockTopChat",
        data() {
            return {
                urlPhoto: this.$store.getters.getServerUrl
            }
        },
        props: {
            sliceTXTMembers: Function,
            wsChat: WebSocket
        },
        methods: {
            ChangeNameChat(event) {
                var parent = event.target.closest('.info-chat');
                var chat_name = parent.querySelector('.chat-name');
                var change_chat_name = parent.querySelector('.change-chat-name');
                var change_name = parent.querySelector('.change-name');
                var btn_change = parent.querySelector('.pencil');
                var btn_save = parent.querySelector('.save');

                chat_name.style.display = 'none';
                change_name.value = chat_name.querySelector('p').innerHTML.trim();
                change_chat_name.style.display = 'inline-block';
                btn_change.style.display = 'none';
                btn_save.style.display = 'block';
                change_name.focus();
            },
            SaveNewNameChat(event) {
                var parent = event.target.closest('.info-chat');
                var chat_name = parent.querySelector('.chat-name');
                var change_chat_name = parent.querySelector('.change-chat-name');
                var change_name = parent.querySelector('.change-name');
                var btn_change = parent.querySelector('.pencil');
                var btn_save = parent.querySelector('.save');
                var innerMessage = document.getElementById('innerMessages');
                var chat_id = innerMessage.getAttribute('data-chat_id');

                chat_name.style.display = 'inline-block';
                if (change_name.value.trim().length > 149) {
                    chat_name.querySelector('p').innerHTML = change_name.value.trim().slice(0, 150) + '...'
                } else {
                    chat_name.querySelector('p').innerHTML = change_name.value.trim();
                }
                var chat = document.getElementById('chat-' + chat_id);
                var chat_name_left = chat.querySelector('.chat-members-list');
                chat_name_left.innerHTML = change_name.value.trim();
                this.sliceTXTMembers(chat_name_left);

                change_chat_name.style.display = 'none';
                btn_change.style.display = 'block';
                btn_save.style.display = 'none';
                this.wsChat.send(JSON.stringify({
                    action: 'change_chat_name',
                    message: change_name.value.trim()
                }))
            }
        }
    }
</script>

<style scoped>

</style>
