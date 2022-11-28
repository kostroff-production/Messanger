<template>
    <div>
        <div id="message_form">
            <div id="message-form" class="panel panel-body">
                <div id="message_id div" tabindex="0" contenteditable="true" data-placeholder="Ваше сообщение...."></div>

                <div class="right-menu">

                    <div id="emoji-box-base" class="emoji-box-base">
                        <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-emoji-smile" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                          <path fill-rule="evenodd" d="M4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683z"/>
                          <path d="M7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5z"/>
                        </svg>
                    </div>
                    <div id="add-file" class="add-file">
                        <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-paperclip" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M4.5 3a2.5 2.5 0 0 1 5 0v9a1.5 1.5 0 0 1-3 0V5a.5.5 0 0 1 1 0v7a.5.5 0 0 0 1 0V3a1.5 1.5 0 1 0-3 0v9a2.5 2.5 0 0 0 5 0V5a.5.5 0 0 1 1 0v7a3.5 3.5 0 1 1-7 0V3z"/>
                        </svg>
                    </div>
                    <div id="btnSave" style="display: none">
                        <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-pencil" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M11.293 1.293a1 1 0 0 1 1.414 0l2 2a1 1 0 0 1 0 1.414l-9 9a1 1 0 0 1-.39.242l-3 1a1 1 0 0 1-1.266-1.265l1-3a1 1 0 0 1 .242-.391l9-9zM12 2l2 2-9 9-3 1 1-3 9-9z"/>
                          <path fill-rule="evenodd" d="M12.146 6.354l-2.5-2.5.708-.708 2.5 2.5-.707.708zM3 10v.5a.5.5 0 0 0 .5.5H4v.5a.5.5 0 0 0 .5.5H5v.5a.5.5 0 0 0 .5.5H6v-1.5a.5.5 0 0 0-.5-.5H5v-.5a.5.5 0 0 0-.5-.5H3z"/>
                        </svg>
                    </div>
                    <div id="btn-message-form">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" fill="currentColor" class="bi bi-cursor-fill" viewBox="0 0 16 16">
                          <path d="M14.082 2.182a.5.5 0 0 1 .103.557L8.528 15.467a.5.5 0 0 1-.917-.007L5.57 10.694.803 8.652a.5.5 0 0 1-.006-.916l12.728-5.657a.5.5 0 0 1 .556.103z"/>
                        </svg>
                    </div>

                </div>
                <div class="list-media-file"></div>
            </div>
            <div class="panel panel-body" id="block-message-form">
                <p>** Пользователь ограничил круг лиц, которые могут ему написать. **</p>
            </div>
        </div>
        <div id="drop-menu-add-file">
            <div class="add-menu photo-files">
                <p>Фото</p>
                <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-camera-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path d="M10.5 8.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>
                  <path fill-rule="evenodd" d="M2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2zm.5 2a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1zm9 2.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0z"/>
                </svg>
            </div>
            <div class="add-menu video-files">
                <p>Видео</p>
                <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-camera-reels-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2.667 6h6.666C10.253 6 11 6.746 11 7.667v6.666c0 .92-.746 1.667-1.667 1.667H2.667C1.747 16 1 15.254 1 14.333V7.667C1 6.747 1.746 6 2.667 6z"/>
                  <path d="M7.404 11.697l6.363 3.692c.54.313 1.233-.066 1.233-.697V7.308c0-.63-.693-1.01-1.233-.696l-6.363 3.692a.802.802 0 0 0 0 1.393z"/>
                  <circle cx="3" cy="3" r="3"/>
                  <circle cx="9" cy="3" r="3"/>
                </svg>
            </div>
        </div>
        <div class="add-photo" style="display: none">
            <div class="photo-file">
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                  <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                </svg>
                <div class="content-photo">

                </div>
                <div class="backgroundDiv">
                </div>
            </div>
        </div>
        <div class="add-video" style="display: none">
            <div class="video-file">
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                  <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                </svg>
                <video controls="controls">
                    <source src="#" type="video/mp4">
                </video>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "MessageForm",
        props: {
            wsChat: WebSocket,
            urlServer: String,
            urlPhoto: String,
            mobile: Boolean,
            triggerWS: Boolean
        },
        emits: ['FormInputPhoto', 'FormInputVideo',
            'backgroundDiv', 'funcCreateMessage', 'funcHideSave', 'outWsMF',
            'fun_click'
        ],
        data: function () {
            return {
                drop_menu_add: null,
                add_file: null,
                backgroundDivForm: null,
                loadingDivPhoto: null,
                loadingDivVideo: null,
                AddPhotos: null,
                VideoForm: null,
                content: null,
                btn_info: null,
                info_div: null,
                btn_info_photo: null,
                btn_info_video: null,
                str_image: '',
                str_video: '',
                input_div: null,
                btn_form: null,
                blockMedia: null,
                PhotoBox: null,
                VideoBox: null,
                inputPhoto: null,
                btnPhoto: null,
                stop_photo: null,
                inputVideo: null,
                btnVideo: null,
                stop_video: null,
                btnSave: null,
                innerMessage: null,
                token: localStorage.getItem('authToken').match(/Kostrov\s(.+)/)[1],
                id_photo_message_p: null,
                id_video_p: null,
                wsPhotoMessage: null,
                wsVideo: null
            }
        },
        mounted() {
            this.innerMessage = document.getElementById('innerMessages');
            this.add_file = document.getElementById('add-file');
            this.drop_menu_add = document.getElementById('drop-menu-add-file');
            this.backgroundDivForm = document.getElementById('backgroundDivForm');
            this.$emit('backgroundDiv', this.backgroundDivForm);
            this.loadingDivPhoto = document.getElementById('loading-photo');
            this.loadingDivVideo = document.getElementById('loading-video');
            this.AddPhotos = document.getElementById('AddPhotos');
            this.$emit('FormInputPhoto', this.AddPhotos);
            this.VideoForm = document.getElementById('AddVideo');
            this.$emit('FormInputVideo', this.VideoForm);
            this.content = document.querySelector('.media_content_div.active-grid');
            this.btn_info = document.getElementById('btn-info-chat');
            this.info_div = document.querySelector('.media-files-chat-body');
            this.btn_info_photo = document.getElementById('med2-1');
            this.btn_info_video = document.getElementById('med2-2');
            this.input_div = document.getElementById('message_id div');
            this.btn_form = document.getElementById('btn-message-form');
            this.blockMedia = document.querySelector('.list-media-file');
            this.PhotoBox = document.querySelector('.add-photo');
            this.VideoBox = document.querySelector('.add-video');
            this.btnSave = document.getElementById('btnSave');

            this.btnSave.onclick = this.hideSave;
            this.$emit('funcHideSave', this.hideSave);
            this.$emit('funcCreateMessage', this.CreateMessage);

            this.innerMessage.onclick = this.edit;

            this.wsPhotoMessage = new WebSocket('ws://' + this.urlServer + '/ws/add/photo/message/?token=' + this.token);

            this.wsPhotoMessage.onopen = () => {
                console.log('connect photo')
            };

            this.inputPhoto = document.getElementById('id_photo_message');
            this.btnPhoto = document.getElementById('btn-photo');
            this.id_photo_message_p = document.getElementById('id_photo_message_p');

            this.inputPhoto.onchange = () => {
                if (this.inputPhoto.files.length > 0) {
                    this.id_photo_message_p.style.display = 'block';
                    this.id_photo_message_p.innerText = this.inputPhoto.files[0].name;
                }
            };

            this.btnPhoto.onclick = (event) => {
                event.preventDefault();
                var files = this.inputPhoto.files;

                if (files.length > 0) {
                    this.BytesFile(files[0]);
                }
            };

            this.wsVideo = new WebSocket('ws://' + this.urlServer + '/ws/add/video/?token=' + this.token);

            this.wsVideo.onopen = () => {
              console.log('connect video')
            };

            var data = {
                wsPhotoMessage: this.wsPhotoMessage,
                wsVideo: this.wsVideo
            };
            this.$emit('outWsMF', data);

            this.inputVideo = document.getElementById('id_video');
            this.btnVideo = document.getElementById('btn-video');
            this.id_video_p = document.getElementById('id_video_p');

            this.inputVideo.onchange = () => {
                if (this.inputVideo.files.length > 0) {
                    this.id_video_p.style.display = 'block';
                    this.id_video_p.innerText = this.inputVideo.files[0].name;
                }
            };

            this.btnVideo.onclick = (event) => {
                event.preventDefault();
                var files = this.inputVideo.files;

                if (files.length > 0) {
                    this.btnVideo.style.display = 'none';
                    this.BytesFile(files[0]);
                }
            };

            this.btn_form.onclick = this.CreateMessage;
            document.querySelector('.bi.bi-cursor-fill').onclick = this.CreateMessage;
            this.input_div.onkeyup = this.CreateMessage;

            this.btn_info_photo.onclick = this.Grid;
            this.btn_info_video.onclick = this.Grid;

            this.btn_info.onclick = () => {
                if (this.info_div.style.display === 'none') {
                    this.info_div.style.display = 'block';
                    this.resizeAll();
                } else {
                    this.info_div.style.display = 'none';
                }
            };

            var data_click = {
                toggleAddMenu: this.toggleAddMenu,
                showFormAddPhoto: this.showFormAddPhoto,
                showFormAddVideo: this.showFormAddVideo,
                gallery: this.gallery
            };
            this.$emit('fun_click', data_click);

            this.wsPhotoMessage.onmessage = e => this.messPhotoMessage(e);
            this.wsVideo.onmessage = e => this.messVideo(e);

            this.wsVideo.onclose = () => this.restartWS();
        },
        methods: {
            restartWS () {
                if (this.triggerWS) {
                    this.wsPhotoMessage = new WebSocket('ws://' + this.urlServer + '/ws/add/photo/message/?token=' + this.token);
                    this.wsPhotoMessage.onopen = () => {
                        console.log('connect photo')
                    };
                    this.wsPhotoMessage.onmessage = e => this.messPhotoMessage(e);

                    this.wsVideo = new WebSocket('ws://' + this.urlServer + '/ws/add/video/?token=' + this.token);
                    this.wsVideo.onopen = () => {
                        console.log('connect video')
                    };
                    this.wsVideo.onmessage = e => this.messVideo(e);
                    this.wsVideo.onclose = () => this.restartWS();

                    var data = {
                        wsPhotoMessage: this.wsPhotoMessage,
                        wsVideo: this.wsVideo
                    };
                    this.$emit('outWsMF', data);
                }
            },
            messPhotoMessage (e) {
                var data_photo = JSON.parse(e.data);
                this.StopPhotoFlicker();
                this.loadingDivPhoto.removeAttribute('style');
                this.inputPhoto.value = '';
                this.id_photo_message_p.style.display = 'none';
                this.AddPhotos.style.display = 'none';
                this.backgroundDivForm.style.display = 'none';

                var addPhotoDiv = this.PhotoBox.querySelector('.photo-file');
                var clone = addPhotoDiv.cloneNode(true);
                var btn_x = clone.querySelector('.bi.bi-x');
                btn_x.onclick = this.DeleteFile;
                var content = clone.querySelector('.content-photo');
                var img = document.createElement('img');
                img.setAttribute('data-id', data_photo.data[0]);
                img.src = this.urlPhoto + '/media/' + data_photo.data[1];
                content.appendChild(img);
                this.blockMedia.appendChild(clone);
                this.str_image += data_photo.data[0] + ',';

                var media_1 = document.getElementById('med-1');
                var media_photo = document.getElementById('photo-media');
                var clone_media_photo = media_photo.cloneNode(true);
                clone_media_photo.setAttribute('id', 'media-photo-' + data_photo.data[0]);
                var img_media = clone_media_photo.querySelector('img');
                img_media.src = this.urlPhoto + '/media/' + data_photo.data[1];
                media_1.appendChild(clone_media_photo);
            },
            messVideo (e) {
                var data_video = JSON.parse(e.data);
                this.StopVideoFlicker();
                this.loadingDivVideo.removeAttribute('style');
                this.inputVideo.value = '';
                this.id_video_p.style.display = 'none';
                this.VideoForm.style.display = 'none';
                this.backgroundDivForm.style.display = 'none';

                var addVideoDiv = this.VideoBox.querySelector('.video-file');
                var clone = addVideoDiv.cloneNode(true);
                var btn_x = clone.querySelector('.bi.bi-x');
                btn_x.onclick = this.DeleteFile;
                var video = clone.querySelector('video');
                video.setAttribute('data-id', data_video[0]);
                var source = clone.querySelector('source');
                source.src = this.urlPhoto + '/media/' + data_video[1];
                this.blockMedia.appendChild(clone);
                this.str_video += data_video[0] + ',';

                var media_2 = document.getElementById('med-2');
                var media_video = document.getElementById('video-media');
                var clone_media_video = media_video.cloneNode(true);
                clone_media_video.setAttribute('id', 'media-video-' + data_video[0]);
                var source_media = clone_media_video.querySelector('source');
                source_media.src = this.urlPhoto + '/media/' + data_video[1];
                media_2.appendChild(clone_media_video);
            },
            CreateMessage(event) {
                if (this.input_div.hasAttribute('data-message-slug') === false) { // проверяем наличие атрибута "обновление сообщения"
                    var target = event.target;
                    // очищаем текст сообщения от пробелов и добавляем содержимое блока с медиа файлами
                    var str = this.input_div.innerHTML.replace(/&nbsp;+|<div>+|<\/div>+|<br>+/g, ' ').trim();
                    var media = this.blockMedia.innerHTML;
                    if (str !== '' || media !== '') { // проверяем, что бы инпут был не пустой
                        if (target.parentElement.id === "message-form" && event.keyCode === 13) { // отправляем сообщение если нажат enter
                            this.add_media_in_message();
                            if (media !== '') {
                                this.wsChat.send(JSON.stringify({
                                    action: 'create_message_file',
                                    message: str + this.blockMedia.innerHTML,
                                    img: this.str_image.replace(/,$/, ''),
                                    video: this.str_video.replace(/,$/, '')
                                }));
                            } else {
                                this.wsChat.send(JSON.stringify({
                                    action: 'create_message',
                                    message: str
                                }));
                            }
                            this.input_div.innerHTML = '';
                            this.blockMedia.innerHTML = '';
                            this.str_image = '';
                            this.str_video = '';
                        }

                        if (target.parentElement.id === "btn-message-form") { // отправляем сообщение если нажата кнопка "отправки"
                            this.add_media_in_message();
                            if (media !== '') {
                                this.wsChat.send(JSON.stringify({
                                    action: 'create_message_file',
                                    message: str + this.blockMedia.innerHTML,
                                    img: this.str_image.replace(/,$/, ''),
                                    video: this.str_video.replace(/,$/, '')
                                }));
                            } else {
                                this.wsChat.send(JSON.stringify({
                                    action: 'create_message',
                                    message: str
                                }));
                            }
                            this.input_div.innerHTML = '';
                            this.blockMedia.innerHTML = '';
                            this.str_image = '';
                            this.str_video = '';
                        }
                    }else {
                        this.input_div.innerHTML = '';
                        target.blur(); // если инупс пуст и мы пытемся отправить сообщение, то таргет сбрасывается
                    }
                }
            },
            UpdateMessage(event) { // работа функции схожа с функцией создания сообщения
                if (this.input_div.hasAttribute('data-message-slug')) {
                    var target = event.target;
                    var slug = this.input_div.getAttribute('data-message-slug');

                    var media = this.blockMedia.innerHTML;
                    var str = this.input_div.innerHTML.replace(/&nbsp;+|<div>+|<\/div>+|<br>+/g, ' ').trim();
                    if (str !== '' || media !== '') {
                        if (target.parentElement.id === "message-form" && event.keyCode === 13) {
                            this.add_media_in_message();
                            if (this.str_image !== '' || this.str_video !== '') {
                                this.wsChat.send(JSON.stringify({
                                    action: 'update_message_file',
                                    slug_message: slug,
                                    message: str + this.blockMedia.innerHTML,
                                    img: this.str_image.replace(/,$/, ''),
                                    video: this.str_video.replace(/,$/, '')
                                }));
                            } else {
                                this.wsChat.send(JSON.stringify({
                                    action: 'update_message',
                                    slug_message: slug,
                                    message: str + this.blockMedia.innerHTML
                                }));
                            }
                            this.hideSave();
                            this.input_div.innerHTML = '';
                            this.blockMedia.innerHTML = '';
                            this.str_image = '';
                            this.str_video = '';
                            this.input_div.removeAttribute('data-message-slug');
                            this.input_div.removeAttribute('data-message-id');
                            this.input_div.onkeyup = this.CreateMessage;
                            target.blur();
                        }

                        if (target.parentElement.id === "btnSave") {
                            this.add_media_in_message();
                            if (this.str_image !== '' || this.str_video !== '') {
                                this.wsChat.send(JSON.stringify({
                                    action: 'update_message_file',
                                    slug_message: slug,
                                    message: str + this.blockMedia.innerHTML,
                                    img: this.str_image.replace(/,$/, ''),
                                    video: this.str_video.replace(/,$/, '')
                                }));
                            } else {
                                this.wsChat.send(JSON.stringify({
                                    action: 'update_message',
                                    slug_message: slug,
                                    message: str + this.blockMedia.innerHTML
                                }));
                            }
                            this.hideSave();
                            this.input_div.innerHTML = '';
                            this.blockMedia.innerHTML = '';
                            this.str_image = '';
                            this.str_video = '';
                            this.input_div.removeAttribute('data-message-slug');
                            this.input_div.removeAttribute('data-message-id');
                            this.input_div.onkeyup = this.CreateMessage;
                            target.blur();
                        }
                    }else {
                        this.hideSave();
                        this.input_div.innerHTML = '';
                        this.blockMedia.innerHTML = '';
                        this.input_div.removeAttribute('data-message-slug');
                        this.input_div.removeAttribute('data-message-id');
                        this.input_div.onkeyup = this.CreateMessage;
                        target.blur();
                    }
                }
            },
            edit(event) {
                var targ_edit = event.target.closest('.edit-message');
                var targ_delete = event.target.closest('.btn-delete-message');
                var message = event.target.closest('.message-box-user');
                if (message) {
                    var slug = message.getAttribute('data-message-slug');
                }

                if (targ_edit) {
                    var data_id = message.getAttribute('data-message-id');
                    var message_id = document.getElementById(data_id);
                    var btnSave = document.getElementById('btnSave');
                    this.input_div.innerHTML = message_id.innerHTML + '&nbsp';
                    var input_gallery_items = this.input_div.querySelectorAll('.gallery-item.re-post');
                    var gallery_items = message.querySelectorAll('.gallery-item.re-post');

                    for (var i = 0; i < gallery_items.length; i++) {
                        var copy = gallery_items[i].cloneNode(true);
                        this.blockMedia.appendChild(copy);
                        if (input_gallery_items[i]) {
                            input_gallery_items[i].remove();
                        }
                    }

                    var input_video_teg = this.input_div.querySelectorAll('.video-file.create-file');
                    var video_teg = message.querySelectorAll('.video-file.create-file');

                    for (var e = 0; e < video_teg.length; e++) {
                        var copy2 = video_teg[e].cloneNode(true);
                        this.blockMedia.appendChild(copy2);
                        if (input_video_teg[e]) {
                            input_video_teg[e].remove();
                        }
                    }

                    this.edit_media_in_message();
                    this.input_div.setAttribute('data-message-id', data_id);
                    this.input_div.setAttribute('data-message-slug', slug);
                    btnSave.onclick = this.UpdateMessage;
                    this.input_div.onkeyup = this.UpdateMessage;
                    this.input_div.focus();
                    var select = window.getSelection();
                    select.selectAllChildren(this.input_div);
                    select.collapseToEnd();
                    this.hidePen();
                }

                if (targ_delete) {
                    var photo_obj = message.querySelectorAll('img[data-id]');
                    if (photo_obj) {
                        for (var i = 0; i < photo_obj.length; i++) {
                            var photo_id = photo_obj[i].getAttribute('data-id');
                            this.wsChat.send(JSON.stringify({
                                action: 'delete_photo',
                                message: photo_id
                            }));
                        }
                    }
                    var video_obj = message.querySelectorAll('video[data-id]');
                    if (video_obj) {
                        for (var i = 0; i < video_obj.length; i++) {
                            var video_id = video_obj[i].getAttribute('data-id');
                            this.wsChat.send(JSON.stringify({
                                action: 'delete_video',
                                message: video_id
                            }));
                        }
                    }
                    this.wsChat.send(JSON.stringify({
                        action: 'delete_message',
                        message: slug
                    }));
                }
            },
            add_media_in_message() {
                var btnCancel = this.blockMedia.querySelectorAll('.bi.bi-x');
                if (btnCancel) { // удаляем кнопку "удаления" из блока с вложенными медиа файлами
                    for (var i = 0; i < btnCancel.length; i++) {
                        btnCancel[i].style.display = 'none';
                    }
                }
                var photo = this.blockMedia.querySelectorAll('.photo-file');
                if (photo) { // меняем имя класса для фото файлов, что бы подключились необходимые стили
                    for (var e = 0; e < photo.length; e++) {
                        photo[e].classList.remove('photo-file');
                        photo[e].classList.add('gallery-item');
                        photo[e].classList.add('re-post');
                    }
                }
                var video = this.blockMedia.querySelectorAll('.video-file');
                if (video) {
                    for (var s = 0; s < video.length; s++) {
                        video[s].classList.add('create-file')
                    }
                }
            },
            edit_media_in_message() {
                var btnCancel = this.blockMedia.querySelectorAll('.bi.bi-x');
                if (btnCancel) { // удаляем кнопку "удаления" из блока с вложенными медиа файлами
                    for (var i = 0; i < btnCancel.length; i++) {
                        btnCancel[i].style.display = 'block';
                        btnCancel[i].onclick = this.DeleteFile;
                    }
                }
                var photo = this.blockMedia.querySelectorAll('.gallery-item');
                if (photo) { // меняем имя класса для фото файлов, что бы подключились необходимые стили
                    for (var e = 0; e < photo.length; e++) {
                        photo[e].classList.remove('gallery-item');
                        photo[e].classList.remove('re-post');
                        photo[e].classList.add('photo-file');
                    }
                }
                var video = this.blockMedia.querySelectorAll('.video-file');
                if (video) {
                    for (var s = 0; s < video.length; s++) {
                        video[s].classList.remove('create-file')
                    }
                }
            },
            PhotoFlicker() {
                this.stop_photo = setInterval(() => {
                    $('#loading-photo').fadeOut(1000).fadeIn(1000);
                }, 2500);
            },
            StopPhotoFlicker() {
                clearTimeout(this.stop_photo);
            },
            VideoFlicker() {
                this.stop_video = setInterval(() => {
                    $('#loading-video').fadeOut(1000).fadeIn(1000);
                }, 2500);
            },
            StopVideoFlicker() {
                clearTimeout(this.stop_video);
            },
            Grid(event) {
                var fade_info = document.querySelectorAll('.active-grid');
                for (var i = 0; i < fade_info.length; i++) {
                    fade_info[i].classList.remove('active-grid');
                }
                var target = event.target.closest('.med-2');
                this.content = target.querySelector('.media_content_div');
                this.content.classList.add('active-grid');
                var info_box = target.querySelectorAll('.media-info-chat');
                for (var i = 0; i < info_box.length; i++) {
                    info_box[i].classList.add('active-grid');
                }
                this.resizeAll();
            },
            getVal (elem, style) {
                return parseInt(window.getComputedStyle(elem).getPropertyValue(style));
            },
            getHeight (item) {
                return item.querySelector('.media-content').getBoundingClientRect().height;
            },
            resizeAll () {
                var altura = this.getVal(this.content, 'grid-auto-rows');
                var gap = this.getVal(this.content, 'grid-row-gap');
                this.content.querySelectorAll('.media-info-chat.active-grid').forEach((item) => {
                    var el = item;
                    el.style.gridRow = "span " + Math.ceil((this.getHeight(item) + gap) / (altura + gap));
                });
            },
            toggleAddMenu(target) {
                if (target.closest('.add-file')) {
                    $('#drop-menu-add-file').fadeToggle(500);
                    this.showDropMenu();
                } else {
                    $('#drop-menu-add-file').fadeOut(500);
                }
            },
            showDropMenu () {
                if (this.mobile) {
                    this.drop_menu_add.style.bottom = 150 + 'px';
                } else {
                    this.drop_menu_add.style.top = 625 + 'px';
                }
                this.drop_menu_add.style.left = this.add_file.offsetLeft - 120 + 'px';
            },
            showFormAddPhoto() {
                this.backgroundDivForm.style.display = 'block';
                this.AddPhotos.style.display = 'block';
                this.AddPhotos.style.left = (document.body.offsetWidth - this.AddPhotos.offsetWidth) / 2 + 'px';
                this.AddPhotos.style.top = this.AddPhotos.offsetHeight + 'px';
            },
            showFormAddVideo() {
                this.backgroundDivForm.style.display = 'block';
                this.VideoForm.style.display = 'block';
                this.btnVideo.style.display = 'block';
                // позиционируем форму
                this.VideoForm.style.left = (document.body.offsetWidth - this.VideoForm.offsetWidth) / 2 + 'px';
                this.VideoForm.style.top = this.VideoForm.offsetHeight / 2 + 'px';
            },
            gallery(target) {
                var item = target.closest('.gallery-item');
                if (item) {
                    var image = item.querySelector('img');
                    if (item.classList.toggle('full')) {
                        if (this.mobile) {
                            if (image.offsetWidth - image.offsetHeight > 0) {
                                image.style.top = image.offsetHeight / 2 + 'px';
                                image.style.left = 0;
                            } else {
                                image.style.width = 80 + '%';
                                image.style.left = (document.body.offsetWidth - image.offsetWidth) / 2 + 'px';
                                if (image.offsetHeight > 500) {
                                    image.style.top = (image.offsetHeight / 10) / 2 + 'px';
                                } else {
                                    image.style.top = image.offsetHeight / 4 + 'px';
                                }
                            }
                        } else {
                            image.style.top = (document.body.offsetHeight - image.offsetHeight) + 'px';
                            image.style.left = (document.body.offsetWidth - image.offsetWidth) / 2 + 'px';
                        }
                    } else {
                        image.removeAttribute('style');
                    }
                }
            },
            hidePen() {
                $('#btn-message-form').fadeOut(1000);
                setTimeout(() => {
                    $('#btnSave').fadeIn(1000);
                }, 1000);
            },
            hideSave () {
               $('#btnSave').fadeOut(1000);
               setTimeout(function () {
                   $('#btn-message-form').fadeIn(1000);
               }, 1000);
            },
            DeleteFile(event) {
                var obj;
                // проверяем, что удалять
                if (event.target.closest('.photo-file')) {
                    obj = event.target.closest('.photo-file');
                    var photo_id = obj.querySelector('img').getAttribute('data-id');
                    this.wsChat.send(JSON.stringify({
                        action: 'delete_photo',
                        message: photo_id
                    }));
                    var arrPhoto = this.str_image.split(',');
                    for (var i = 0; i < arrPhoto.length; i++) {
                        if (arrPhoto[i] === photo_id) {
                            arrPhoto.splice(i, 1)
                        }
                    }
                    this.str_image = arrPhoto.join(',');
                } else if (event.target.closest('.video-file')) {
                    obj = event.target.closest('.video-file');
                    var video_id = obj.querySelector('video').getAttribute('data-id');
                    this.wsChat.send(JSON.stringify({
                        action: 'delete_video',
                        message: video_id
                    }));
                    var arrVideo = this.str_video.split(',');
                    for (var i = 0; i < arrVideo.length; i++) {
                        if (arrVideo[i] === video_id) {
                            arrVideo.splice(i, 1)
                        }
                    }
                    this.str_video = arrVideo.join(',');
                }
                obj.remove(); // удаляем файл из блока хранения
            },
            BytesFile(file) {
                var content_types = ['video/x-msvideo', 'video/mp4', 'video/mpeg', 'video/wmv', 'video/webm', 'video/ogg', "video/quicktime"];
                if (file.type.match(/(^\w+)\//)[1] === 'image' && file.size <= 104857600) {
                    this.loadingDivPhoto.style.display = 'block';
                    this.PhotoFlicker();
                    this.wsPhotoMessage.send(file);
                } else if (content_types.includes(file.type) && file.size <= 104857600) {
                    this.loadingDivVideo.style.display = 'block';
                    this.VideoFlicker();
                    this.wsVideo.send(file);
                } else {
                     alert('Вы загружаете не поддерживаемый формат ' +
                         'файла или размер файла слишком велик.' +
                         ' Для фото и видео не больше 100 Мб.')
                }
            }
        }
    }
</script>

<style scoped>

</style>
