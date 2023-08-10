<template>
  <div>
    <!-- Your component content here -->
    <el-button @click="downloadPDF">Download PDF</el-button>
    <!--    <el-text ref="compToDownload">123</el-text>-->
    <el-date-picker ref="compToDownload" />
  </div>
</template>
<script setup>
import html2pdf from "html2pdf.js";
const downloadPDF = async (content) => {
  // const content = this.componentToDownload; // Reference to the component you want to download
  console.log(content);
  // const content = this.compToDownload; // Reference to the component you want to download
  const pdfOptions = {
    margin: 10,
    filename: "downloaded-file.pdf",
    image: { type: "jpeg", quality: 0.98 },
    html2canvas: { scale: 2 },
    jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
  };

  try {
    const customContent = "<div><el-date-picker/></div>";
    // const pdf = await html2pdf()
    //   .set(pdfOptions)
    //   .from(content.$el)
    //   .outputPdf();
    // .save();
    const pdf = await html2pdf().set(pdfOptions).from(content).outputPdf();
    const blob = new Blob([pdf], { type: "application/pdf" });
    const url = URL.createObjectURL(blob);

    // Create a link element and click it to trigger the download
    const link = document.createElement("a");
    link.href = url;
    link.download = pdfOptions.filename;
    link.click();
    //
    // // Clean up
    URL.revokeObjectURL(url);
  } catch (error) {
    console.error("Error generating PDF:", error);
  }
};
</script>

<!--<script>-->
<!--import html2pdf from "html2pdf.js";-->

<!--export default {-->
<!--  name: "PdfDownload",-->
<!--  props: {-->
<!--    componentToDownload: Object,-->
<!--  },-->
<!--  methods: {-->

<!--  },-->
<!--};-->
<!--</script>-->
