<template>
  <div>
    <!--    <form @submit.prevent="submitForm">-->
    <!--      <label for="name">Name:</label>-->
    <!--      <input type="text" id="name" v-model="formData.name" required />-->

    <!--      <label for="email">Email:</label>-->
    <!--      <input type="email" id="email" v-model="formData.email" required />-->

    <!--      <label for="message">Message:</label>-->
    <!--      <textarea id="message" v-model="formData.message" required></textarea>-->

    <!--      <button type="submit">Submit</button>-->
    <!--    </form>-->

    <el-divider />

    <el-row>
      <div class="uploadDemo">
        <el-col>
          <el-input
            v-model="demo"
            type="textarea"
            style="width: 20rem"
            :autosize="{ minRows: 5, maxRows: 10 }"
            placeholder="请输入json格式"
          ></el-input>
        </el-col>
        <el-col class="mv-1">
          <el-upload
            class="upload-demo"
            ref="upload"
            accept=".json"
            action=""
            :on-change="changeDemoFile"
            :file-list="demoFileList"
            :auto-upload="false"
          >
            <template #trigger>
              <el-button size="small" type="primary">选取文件填充 </el-button>
            </template>
            <span class="ml-1">
              <el-text>{{ message }}</el-text>
            </span>
          </el-upload>
        </el-col>
      </div>
    </el-row>
    <el-divider />
    <div>
      <el-text>{{ cvResult }}</el-text>
    </div>
    <el-button @click="downloadCV">下载简历</el-button>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, Raw } from "vue";

import type { UploadInstance, UploadUserFile } from "element-plus";

const upload = ref<UploadInstance>();

let demo = ref("");
let demoFileList = ref([] as UploadUserFile[]);
let message = ref("");

const changeDemoFile = (file: File | Raw<any>, demoFileList: void[]) => {
  if (demoFileList.length == 2) {
    //只保留最新的文件
    demoFileList.shift();
  }
  if (file.name.slice(-5) != ".json") {
    alert("只能读取json文件，请重新选择");
  } else {
    // console.log(file.raw);
    let fileReader = new FileReader();
    fileReader.onload = async (e) => {
      try {
        let document = JSON.parse(e.target?.result as string);
        console.log(document);
        demo.value = JSON.stringify(document);
        if (isJSON(demo.value)) {
          message.value = "满足json格式";
        } else {
          message.value = "不满足json格式，请重新选择文件或修改文件";
          upload.value?.clearFiles();
          demo.value = "";
        }
      } catch (err) {
        console.log(err);
        upload.value?.clearFiles();
        message.value = "不满足json格式，请重新选择文件或修改文件";
        demo.value = "";
      }
    };
    fileReader.readAsText(file.raw);
    // TODO: 赋值给cvJson
  }
};

const isJSON = (str: any) => {
  // 判断一个string是否是json类型，用于格式校验
  if (typeof str == "string") {
    try {
      let obj = JSON.parse(str);
      return typeof obj == "object" && obj;
    } catch (e) {
      console.log("error：" + str + "!!!" + e);
      return false;
    }
  }
  console.log("It is not a string!");
};

// interface FormData {
//   name: string;
//   email: string;
// }
// const formData = reactive<FormData>({
//   name: "",
//   email: "",
// });

const cvResult = ref<string>("");
let cvJson = reactive({});

// const submitForm = () => {
//   // 将 formData 转换为 JSON 格式
//   const jsonData = JSON.stringify(formData);

// 使用 Axios 发送 JSON 数据到后端
// axios
//   .post("/your-backend-api-url", jsonData, {
//     headers: {
//       "Content-Type": "application/json",
//     },
//   })
//   .then((response) => {
//     // 处理响应结果
//     console.log("Response from server:", response.data);
//     cvResult.value = "生成成功的返回值";
//   })
//   .catch((error) => {
//     // 处理错误
//     console.error("Error sending data:", error);
//     cvResult.value = "生成失败的返回值";
//   });
// };

const downloadCV = () => {
  // TODO: 下载简历的逻辑
  alert("功能开发中...");
};
</script>

<style scoped></style>
