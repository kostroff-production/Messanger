<template>
    <div id="messages">
        <div id="innerMessages" data-chat_id="0"></div>

        <div class="scroll-bottom-parent">
            <div class="scroll-bottom">
                <svg width="2.5em" height="2.5em" viewBox="0 0 16 16" class="bi bi-chevron-compact-down" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M1.553 6.776a.5.5 0 0 1 .67-.223L8 9.44l5.776-2.888a.5.5 0 1 1 .448.894l-6 3a.5.5 0 0 1-.448 0l-6-3a.5.5 0 0 1-.223-.67z"/>
                </svg>
            </div>
        </div>

        <div class="message-box-user" id="message-box-user" style="display: none" :data-user="person.id">
            <div class="message-menu">
                 <li class="message-menu">
                     <div class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                         <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-three-dots-vertical" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                        </svg>
                     </div>
                    <ul class="dropdown-menu message">
                        <li>
                            <div class="edit-message">
                                <p>Редактировать</p>
                                <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-pencil-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456l-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                                </svg>
                            </div>
                            <div class="btn-delete-message">
                                <p>Удалить</p>
                                <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-trash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                  <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                  <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                </svg>
                            </div>
                        </li>
                    </ul>
                </li>
            </div>
            <div class="message-body-user">
                <ul class="list-inline message">
                    <li class="pull-right text-muted"><small class="message-date-pub-user"></small></li>
                </ul>
                <div class="create-item-message-id">
                    <p></p>
                </div>
            </div>
            <div class="avatar-message-base">
                <img v-if="person.avatar" :src="urlPhoto + person.avatar.photo" alt="" class="img-circle avatar-message">
                <img v-else :src="urlPhoto + '/static/default_avatar.jpg'" alt="" class="img-circle avatar-message">
            </div>
        </div>

        <div class="message-box-friend" id="message-box-friend" style="display: none">
            <div class="avatar-friend">
                <img :src="urlPhoto + '/static/default_avatar.jpg'" alt="" class="img-circle avatar-message">
            </div>
            <div class="message-body">
                <ul class="list-inline">
                    <li class="drop-left-padding">
                        <strong class="message-author"></strong>
                    </li>
                    <li class="pull-right text-muted"><small class="message-date-pub"></small></li>
                </ul>
                <div class="item-message-id">
                    <p></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Messages",
        props: {
            person: Object,
            urlPhoto: String,
            wsMessages: WebSocket,
            change_chat: Boolean
        },
        emits: ['deactivateChangeChat'],
        data () {
            return {
                quantity_start: 10,
                quantity_finish: 20,
                innerMessage: null,
                scroll_btn: null
            }
        },
        updated() {
            this.innerMessage = document.getElementById('innerMessages');
            this.innerMessage.onscroll = this.get_message_send;
            this.scroll_btn = document.querySelector('.scroll-bottom');
        },
        methods: {
            get_message_send () {
                if (this.innerMessage.scrollTop === 0 && this.innerMessage.childElementCount > 9) {
                    if (this.change_chat) {
                        this.$emit('deactivateChangeChat', false);
                        this.quantity_start = 10;
                        this.quantity_finish = 20;
                    }
                    this.wsMessages.send(JSON.stringify({
                        quantity_start: this.quantity_start,
                        quantity_finish: this.quantity_finish
                    }));
                    this.quantity_start += 10;
                    this.quantity_finish += 10;
                }
                if (this.innerMessage.scrollHeight - this.innerMessage.scrollTop > 2500) {
                    this.scroll_btn.style.display = 'block';
                } else {
                    this.scroll_btn.style.display = 'none';
                }
            }
        }
    }
</script>

<style scoped>

</style>
