function downloadFile(filename, content) {
    const blob = new Blob([content], { type: 'text/plain' });

    // Create a temporary URL for the blob
    const url = window.URL.createObjectURL(blob);

    // Create a link element and set its attributes
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;

    // Append the link element to the DOM and click it to trigger download
    document.body.appendChild(link);
    link.click();

    // Clean up by revoking the URL and removing the link element
    window.URL.revokeObjectURL(url);
    document.body.removeChild(link);
}

function scrollAndSendToServer(repeatCount) {

    if (repeatCount === 100) {
        return;
    }
    setTimeout(function () {
        const filename = `peje_content_${repeatCount}.txt`; // Append repeatCount to filename

        document.documentElement.scrollTop = document.documentElement.scrollHeight;
        var domContent = document.documentElement.outerHTML;
        downloadFile(filename, domContent);

        console.log("performing scroll -> ", repeatCount);
        scrollAndSendToServer(repeatCount + 1);
    }, 5000);

}

scrollAndSendToServer(0);  // Replace 1 with the desired number of repetitions
