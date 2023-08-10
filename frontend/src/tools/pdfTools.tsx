import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import { ElNotification } from "element-plus";

export const downloadPDF = async (compToDownload: HTMLElement) => {
  try {
    const pdf = new jsPDF();
    // console.log(compToDownload);
    // Convert the element to an image using a library like html2canvas
    html2canvas(compToDownload).then((res) => {
      const imgData = res.toDataURL("image/png");
      pdf.addImage(imgData, "PNG", 0, 0, 250, 250); // Adjust the positioning and size
      pdf.save("downloaded.pdf");
    });
    // const imgData = canvas.toDataURL("image/png");

    // Add the image to the PDF
    // pdf.addImage(imgData, "PNG", 0, 0, 250, 250); // Adjust the positioning and size
    // pdf.addImage(imgData, "PNG", 100, 10, 190, 250); // Adjust the positioning and size
    // Save or download the PDF
    // pdf.save("downloaded.pdf");
    ElNotification.success({
      title: "pdf已生成，将自动下载",
      offset: 100,
    });
  } catch (e) {
    console.log(e);
  }
};
