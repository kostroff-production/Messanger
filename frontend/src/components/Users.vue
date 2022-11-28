<template>
    <div>
        <div v-for="user in users">
            <div class="person user" :id="'user-' + user.id">
                <div class="checkPeople">
                    <input :data-user-id="user.id"  type="checkbox" class="check">
                </div>
                <div class="person-avatar">
                    <img v-if="user.avatar" :src="urlPhoto + user.avatar.photo" alt="" class="img-circle avatar-chat">
                    <img v-else :src="urlPhoto + '/static/default_avatar.jpg'"  alt="" class="img-circle avatar-chat">
                </div>
                <div class="person-info">
                    <p v-html="user.name"></p>
                </div>
                <div class="person-menu">
                    <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-caret-left-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path d="M3.86 8.753l5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>
                </div>
                <div class="person-btn">
                    <div class="message-btn" @click="write_message"
                            :data-user="user.id">
                        <p>Написать</p>
                    </div>
                    <div class="subscribe-btn" @click="SendingToAdd"
                        :data-user="user.id">
                        <p>Добавить</p>
                    </div>
                    <div class="unsubscribe-btn" @click="DeleteFriend"
                        :data-friend-user="user.id">
                        <p>Удалить</p>
                    </div>
                    <div class="info-subscribe possible_friends">
                        <i>Ожидает подтверждения</i>
                    </div>
                    <div class="info-subscribe waiting_confirmations">
                        <i>Запрос отправлен</i>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Users",
        props: {
            users: Array,
            friends: Array,
            urlPhoto: String,
            write_message: Function,
            DeleteFriend: Function,
            SendingToAdd: Function
        },
        emits: ['funcSendingToAdd'],
        updated() {
            this.ActivateBTN();
        },
        methods: {
            ActivateBTN() {
                var user = document.querySelectorAll('.person.user');
                for (var i = 0; i < user.length; i++) {
                    var data_id = parseInt(user[i].getAttribute('id').replace(/\w+-/, ''));
                    var subscribe = user[i].querySelector('.subscribe-btn');
                    var unsubscribe = user[i].querySelector('.unsubscribe-btn');
                    var possible = user[i].querySelector('.possible_friends');
                    var waiting = user[i].querySelector('.waiting_confirmations');
                    var tag = 0;
                    for (var e = 0; e < this.friends.length; e++) {
                        if (this.friends[e].friends) {
                            if (this.friends[e].friends.id === data_id) {
                                subscribe.style.display = 'none';
                                possible.style.display = 'none';
                                waiting.style.display = 'none';
                                tag = 1;
                            }
                        } else if (this.friends[e].possible_friends) {
                            if (this.friends[e].possible_friends.id === data_id) {
                                subscribe.style.display = 'none';
                                unsubscribe.style.display = 'none';
                                waiting.style.display = 'none';
                                tag = 1;
                            }
                        } else if (this.friends[e].waiting_confirmations) {
                            if (this.friends[e].waiting_confirmations.id === data_id) {
                                subscribe.style.display = 'none';
                                unsubscribe.style.display = 'none';
                                possible.style.display = 'none';
                                tag = 1;
                            }
                        }
                    }
                    if (tag === 0) {
                        unsubscribe.style.display = 'none';
                        possible.style.display = 'none';
                        waiting.style.display = 'none';
                    }
                }
            }
        }
    }
</script>

<style scoped>
</style>
