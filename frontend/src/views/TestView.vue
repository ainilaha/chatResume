<template>
  <div>
    <el-divider />

    <el-row style="display: flex; justify-content: space-evenly">
      <el-row>
        <el-input
          v-model="question"
          type="textarea"
          style="width: 40vw"
          :autosize="{ minRows: 20, maxRows: 100 }"
          placeholder="请输入问题"
        ></el-input>
      </el-row>
      <el-row>
        <el-divider
          direction="vertical"
          content-position="center"
          style="height: 100%"
        />
      </el-row>
      <el-row>
        <div>
          <el-input
            v-model.trim="queResult"
            type="textarea"
            style="width: 40vw"
            :autosize="{ minRows: 20, maxRows: 100 }"
            placeholder="生成的问题答案会显示在此处"
            readonly
          ></el-input>
        </div>
      </el-row>
    </el-row>
    <el-divider />
    <el-col class="mv-1" style="display: flex; justify-content: center">
      <el-button
        @click="submitQue"
        :loading="loadingStatus"
        :disabled="question.length == 0"
        >提交
      </el-button>
      <el-button
        @click="
          () => {
            loadingStatus2 = true;
            downloadPDF(compToDownload).finally(() => {
              loadingStatus2 = false;
            });
          }
        "
        :disabled="isEmptyObj(jsonResult)"
        :loading="loadingStatus2"
        >下载
      </el-button>
      <el-button
        @click="
          () => {
            question = '';
            queResult = '';
            jsonResult = {};
            // jsonResult.hasContent = false;
          }
        "
        :disabled="loadingStatus || loadingStatus2"
        >清空
      </el-button>
      <!--      <component :is="PdfDownload" componentToDownload="compToDownload" />-->
    </el-col>
  </div>
  <div class="m-3" ref="compToDownload">
    <el-text style="font-weight: bold; font-size: large">简历预览</el-text>
    <JsonDisplay
      class="mt-3"
      v-if="!isEmptyObj(jsonResult)"
      :json-data="jsonResult"
    ></JsonDisplay>
    <div v-else class="mv-1">
      <el-text>请先提交简历信息</el-text>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { isEmptyObj, isJSON } from "@/tools/JsonTools";
import JsonDisplay from "@/components/JsonDisplay.vue";
import jsPDF from "jspdf";
import "jspdf-autotable";
import html2canvas from "html2canvas";
import { ElNotification } from "element-plus";
import { downloadPDF } from "@/tools/pdfTools";
import component from "*.vue"; // If you need tables
const compToDownload = ref(); // Replace with your element ref
let queResult = ref("");
let jsonResult = ref({});
let loadingStatus = ref(false);
let loadingStatus2 = ref(false);
let question = ref("");

// const downloadPDF = async () => {
//   try {
//     loadingStatus2.value = true;
//     const pdf = new jsPDF();
//     console.log(compToDownload);
//     // Convert the element to an image using a library like html2canvas
//     const canvas = await html2canvas(compToDownload.value);
//     const imgData = canvas.toDataURL("image/png");
//
//     // Add the image to the PDF
//     pdf.addImage(imgData, "PNG", 0, 0, 250, 250); // Adjust the positioning and size
//     // pdf.addImage(imgData, "PNG", 100, 10, 190, 250); // Adjust the positioning and size
//
//     // Save or download the PDF
//     pdf.save("downloaded.pdf");
//     ElNotification.success({
//       title: "pdf已生成，将自动下载",
//       offset: 100,
//     });
//   } catch (e) {
//     console.log(e);
//   } finally {
//     loadingStatus2.value = false;
//   }
// };

const submitQue = () => {
  loadingStatus.value = true;
  fetch("http://localhost:5000/submit", {
    method: "POST",
    body: JSON.stringify({
      question: question.value,
    }),
    // mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
      // "Content-Type": "text",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  })
    .then((res) => {
      if (res.ok) {
        res.json().then((data) => {
          let str: string = data.result;
          let str2 = str.substring(str.indexOf("{"), str.lastIndexOf("}") + 1);
          if (isJSON(str2)) {
            queResult.value = JSON.stringify(JSON.parse(str2), null, 4);
            jsonResult.value = JSON.parse(str2);
            // jsonResult.value.hasContent = true;
            ElNotification.success({
              title: "简历生成成功",
              offset: 100,
            });
            // console.log(jsonResult);
          } else {
            queResult.value = str;
            jsonResult.value = {};
          }
          console.log(queResult.value);
        });
      }
    })
    .catch((e) => {
      // FIXME: 异常JSON反馈
      console.log(e);
    })
    .finally(() => {
      loadingStatus.value = false;
    });
};
</script>

<style scoped></style>
