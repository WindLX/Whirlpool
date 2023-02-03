<script>
import axios from "axios";
export default {
    name: 'PicConverter',
    data() {
        return {
            imageUrl: "",
            imageName: "None",
        }
    },
    methods: {
        Upload(event) {
            var file = event.target.files[0];
            if (file == undefined) {
                this.imageName = "None";
                this.imageUrl = "";
            }
            else {
                const isValid =
                    file.type === "image/jpeg" ||
                    file.type === "image/png" ||
                    file.type === "image/jpg" ||
                    file.type == "image/ico";
                if (!isValid) {
                    this.imageName = "UnVaild Picture Type";
                    this.imageUrl = "";
                }
                else {
                    this.imageName = file.name;
                    let src = window.URL.createObjectURL(file);
                    this.imageUrl = src;

                    let param = new FormData();
                    param.append("file", file, file.name);
                    axios({
                        method: "post",
                        url: "http://127.0.0.1:5000/upload",
                        headers: { 'Content-Type': 'multipart/form-data' },
                        data: param
                    })
                    .then(response => {
                        console.log(response);
                    })
                    .catch(function (err) {
                        console.log(err);
                    })
                }
            }
        },
        Converter() {

        },
        Download() {

        },
    }
}
</script>

<template>
    <div class="container">
        <label for="upload" class="btn">Upload</label>
        <input type="file" @change="Upload" id="upload" accept="image/jpg, image/jpeg, image/png, image/ico">
        <span class="line"/>
        <p class="picname">
            {{ imageName }}
        </p>
        <img :src="imageUrl">
        <span class="line"/>
        <div class="type">
            <input type="radio" name="png" value="png">
            <input type="radio" name="png" value="ico">
        </div>
        <button class="btn" @click="Converter()">
            Converter
        </button>
        <div class="load">
            <div class="cube cube1"></div>
            <div class="cube cube2"></div>
            <div class="cube cube3"></div>
            <div class="cube cube4"></div>
            <div class="cube cube5"></div>
            <div class="cube cube6"></div>
            <div class="cube cube7"></div>
            <div class="cube cube8"></div>
            <div class="cube cube9"></div>
        </div>
        <span class="line"/>
        <button class="btn" @click="Download()">
            Download
        </button>
    </div>
</template>

<style>
    * {
        margin: 0;
        padding: 0;
        transition: .2s;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 100px 500px;
    }
    #upload {
        display: none;
    }
    img {
        min-width: 100px;
        min-height: 100px;
        max-height: 300px;
        object-fit: cover;
        margin-top: 20px;
    }
    img:hover {
        box-shadow: 0px 2px 10px #777777;
    }
    .picname {
        font-size: 18px;
    }
    .line {
        padding: 1px 200px;
        background-color: #DFDFDF;
        margin: 20px 0;
    }
    .load {
        width: 40px;
        height: 40px;
        margin: 50px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 0px;
    }
    .load .cube {
        width: 10px;
        height: 10px;
        background-color: #da8fc6;
    }
    .cube7 {
        animation: loadAnimate .8s linear infinite;
        animation-delay: 0s;
    }
    .cube4,
    .cube8 {
        animation: loadAnimate .8s linear infinite;
        animation-delay: .1s;
    }
    .cube1,
    .cube5,
    .cube9 {
        animation: loadAnimate .8s linear infinite;
        animation-delay: 0.2s;
    }
    .cube2,
    .cube6 {
        animation: loadAnimate .8s linear infinite;
        animation-delay: .3s;
    }
    .cube3 {
        animation: loadAnimate .8s linear infinite;
        animation-delay: .4s;
    }
    @keyframes loadAnimate {
        0%,
        70%,
        100% {
            transform: scale3d(1,1,1);
        }
        35% {
            transform: scale3d(0,0,1);
        }
    }
    .btn {
        border: none;
        padding: 20px;
        border-radius: 5px;
        font-size: 18px;
        position: relative;
        text-decoration: none;
        overflow: hidden;
        display: inline-block;
        cursor: pointer;
        background-color: #f0f0f0;
    }
    .btn:hover {
        transform: scale(1.1);
        color: #FFFFFF;
        box-shadow: 0px 2px 10px #777777;
        background-color: #e219ae;
    }
    @keyframes animate {
        0% {
            width: 0px;
            height: 0px;
            opacity: .5;
        }
        100% {
            width: 500px;
            height: 500px;
            opacity: 0;
        }
    }
</style>