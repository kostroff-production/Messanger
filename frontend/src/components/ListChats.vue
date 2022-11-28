<template>
    <div>
        <div v-if="chats.length > 0">
            <div v-for="chat in chats">
                <div class="chat-box-list" :data-chat-id="chat.id" :id="'chat-' + chat.id" @click="changeChatConnect">
                    <div class="chat-list">
                        <div class="chat-reply-body">
                            <ul class="list-inline">
                                <li class="drop-left-padding">
                                    <strong class="chat-members-list">
                                        <div v-if="chat.name" v-html="chat.name"></div>
                                        <div v-else>
                                            <div v-for="member in chat.members">
                                                <div v-if="member.id !== person.id" v-html="member.name"></div>
                                            </div>
                                        </div>
                                    </strong>
                                </li>
                                <div class="pull-right" v-if="chat.last_message">
                                    <li class="pull-right text-muted date-chat"><small v-html="chat.last_message.date_pub"></small></li>
                                </div>
                                <div v-else class="pull-right">
                                    <li class="pull-right text-muted date-chat"><small></small></li>
                                </div>
                                <div class="chat-unread">
                                    <div v-if="chat.last_message" class="pull-right">
                                        <li v-if="chat.last_message.is_read === false && chat.last_message.author.id !== person.id" class="pull-right text-muted"><span class="badge">1</span></li>
                                        <li v-else class="pull-right text-muted"><span class="badge" style="display: none">0</span></li>
                                    </div>
                                    <div v-else class="pull-right">
                                        <li class="pull-right text-muted"><span class="badge" style="display: none">0</span></li>
                                    </div>
                                </div>
                            </ul>
                        </div>
                        <div class="div-avatar-chat">
                            <div v-for="member in chat.members">
                                <div v-if=" member.id !== person.id">
                                    <img v-if="member.avatar" :src="urlPhoto + member.avatar.photo" alt="" class="img-circle avatar-chat">
                                    <img v-else :src="urlPhoto + '/static/default_avatar.jpg'"  alt="" class="img-circle avatar-chat">
                                </div>
                            </div>
                        </div>
                        <div class="chat-list-message">
                            <div class="chat-head">
                                <div v-if="chat.last_message">
                                    <p v-if="chat.last_message.author" class="chat-list-author-message" v-html="chat.last_message.author.name + ':'"></p>
                                    <p v-else class="chat-list-author-message"></p>
                                </div>
                                <div v-else>
                                    <p class="chat-list-author-message"></p>
                                </div>

                            </div>
                            <div class="chat-message">
                                <div v-if="chat.last_message">
                                    <p class="chat-message-p" v-if="chat.last_message.message" v-html="'&nbsp;' + chat.last_message.message"></p>
                                    <p class="chat-message-p" v-else >Сообщение было удалено</p>
                                </div>
                                <div v-else>
                                    <p class="chat-message-p">Сообщение было удалено</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <p :id="'chat-line-' + chat.id" class="chat-line"></p>
            </div>
        </div>
        <div v-else>
            <div class="chat-label chat">Нет ни одного начатого диалога</div>
        </div>

        <div class="chat-box-list" style="display: none" id="chat-id">
            <div class="chat-list">
                <div class="chat-reply-body">
                    <ul class="list-inline">
                        <li class="drop-left-padding">
                            <strong class="chat-members-list"></strong>
                        </li>
                        <li class="pull-right text-muted date-chat"><small></small></li>
                        <div class="chat-unread">
                            <li class="pull-right text-muted"><span class="badge" style="display: none">0</span></li>
                        </div>
                    </ul>
                </div>
                <div class="div-avatar-chat"></div>
                <div class="chat-list-message">
                    <div class="chat-head">
                        <p class="chat-list-author-message"></p>
                    </div>
                    <div class="chat-message">
                        <p class="chat-message-p">*Сообщений пока нет*</p>
                    </div>
                </div>
            </div>
        </div>
        <p id="chat-line-id" class="chat-line"></p>
    </div>
</template>

<script>
    export default {
        name: "ListChats",
        props: {
            chats: Array,
            person: Object,
            wsMessages: WebSocket,
            wsChat: WebSocket,
            wsConnect: WebSocket,
            sliceTXTMembers: Function,
            sliceTXT: Function
        },
        emits: ['activeChangeChat', 'funChangeChatConnect'],
        data: function () {
            return {
                urlPhoto: this.$store.getters.getServerUrl,
                urlServer: this.$store.getters.getServerUrl.replace('http://', ''),
                chat_members_list: null,
                chat_message: null
            }
        },
        mounted() {
            this.$emit('funChangeChatConnect', this.changeChatConnect)
        },
        updated() {
            this.chat_members_list = document.querySelectorAll('.chat-members-list div');
            for (var q = 0; q < this.chat_members_list.length; q++) {
                this.sliceTXTMembers(this.chat_members_list[q]); // собираем все названия чатов и передаем в обрачотчик
            }

            this.chat_message = document.querySelectorAll('.chat-message-p');
            for (var w = 0; w < this.chat_message.length; w++) {
                this.sliceTXT(this.chat_message[w]); // собираем все последние сообщения бесед
            }
        },
        methods: {
            changeChatConnect(event) {
                var parent = event.target.closest('.chat-box-list');
                var chat_id = parent.getAttribute('data-chat-id');
                this.$emit('activeChangeChat', true);
                var scroll_btn = document.querySelector('.scroll-bottom');
                if (scroll_btn) {
                    scroll_btn.style.display = 'none';
                }
                this.wsConnect.send(JSON.stringify({
                    chat_id: chat_id
                }));
            }
        }
    }
</script>

<style scoped>

</style>
