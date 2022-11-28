<template>
<div>
    <div v-if="friends.length > 0">
        <div v-for="friend in friends">
            <div v-if="friend.friends">
                <div class="person" :id="'friend-' + friend.friends.id">
                    <div class="checkPeople">
                        <input :data-user-id="friend.friends.id"  type="checkbox" class="check">
                    </div>
                    <div class="person-avatar">
                        <img v-if="friend.friends.avatar" :src="urlPhoto + friend.friends.avatar.photo" alt="" class="img-circle avatar-chat">
                        <img v-else :src="urlPhoto + '/static/default_avatar.jpg'" alt="" class="img-circle avatar-chat">
                    </div>
                    <div class="person-info">
                        <p v-html="friend.friends.name"></p>
                    </div>
                    <div class="person-menu">
                        <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-caret-left-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path d="M3.86 8.753l5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                        </svg>
                    </div>
                    <div class="person-btn">
                        <div class="message-btn" @click="write_message"
                                :data-user="friend.friends.id">
                            <p>Написать</p>
                        </div>
                        <div class="unsubscribe-btn" @click="DeleteFriend"
                                :data-friend-user="friend.friends.id">
                            <p>Удалить</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-else>
        <div class="chat-label friend">Здесь будут показаны Ваши друзья</div>
    </div>
    </div>
</template>

<script>
    export default {
        name: "Friends",
        props: {
            friends: Array,
            urlPhoto: String,
            write_message: Function,
            DeleteFriend: Function
        }
    }
</script>

<style scoped>

</style>
