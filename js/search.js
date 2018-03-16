/* Load getThreeColumnsOfTable on startup */
window.onload = getThreeColumnsOfTable

/* Array containing words sorted by alohabetical order */
var origWords = new Array();
/*  Array containing files corresponding word in above array*/
var origFiles = new Array();
/* Array containing line nos corresponding to files in above array */
var origLineNo = new Array();

/**/ 
function getAllIndexes(arr, val) {
	var indexes = [], i = -1, count = 0;
	/*printArray(arr);*/
	while ((i = arr.indexOf(val, i+1)) != -1){
		indexes.push(i);
		if( count==0 ) {
			console.log(i);
		}
		count += 1;
	}
	if ( count == 0 ) {
		indexes.push(-1);
	}
	else {
		indexes.push(count);
	}
	return indexes;
}

/* Print Original Dictionary in a table format */
function printOrigDictionary () {
	console.log('printOrigDictionary');
	var t0 = performance.now();
	var wordTable = "<center><table id=\"indexWords\"><thead><tr id=\"head\">";
	wordTable += "<th>Word</th><th>File Name</th><th>Line Nos</th></tr></thead>";
	var len = origWords.length;
	for (var i = 0; i < len; i++) {
		wordTable += "<tr id=\"row\">";
		wordTable += "<td id=\"word\">" + origWords[i] + "</td>";
		wordTable += "<td id=\"file-name\">" + origFiles[i] + "</td>";
		wordTable += "<td id=\"line-nos\">" + origLineNo[i] + "</td>";
		wordTable += "</tr>";
	}
	wordTable += "</table></center>";
	var t1 = performance.now();
	document.getElementById("content").innerHTML = ("<center>Your query took " + (t1 - t0) + " milliseconds to execute.</center><br>");
	document.getElementById("content").innerHTML += (wordTable);
}

/* Search for word typed in search box and make the necessary table output */
function searchWord (word) {
	document.getElementById("content").innerHTML = "";
	document.getElementById("resultBox").innerHTML = "";
	/*var dummyArray = new Array();*/
	/*copyArray(workWords, dummyArray);*/
	/*dummyArray.sort()*/
	var t0 = performance.now();
	var wordSearch = "<center>You've queried for " + word + ". ";
	var wordNotFound = "<center>Word <b>"+word+"</b> not found</center><br>";
	var indexes = getAllIndexes(origWords, word.toLowerCase());
	/*document.getElementById("resultBox").innerHTML += (indexes.length + "<br>");*/
	/*document.getElementById("resultBox").innerHTML += (indexes[indexes.length-1] + "<br>");*/
	if ( indexes.length == 1 && indexes[0] == -1 ) {
		document.getElementById("resultBox").innerHTML += (wordNotFound);
		return -1;
	}
	else {
		var wordTable = "<center><table id=\"indexWords\"><thead><tr id=\"head\">";
		wordTable += "<th>Word</th><th>File Name</th><th>Line Nos</th></tr></thead>";
		/*document.getElementById("resultBox").innerHTML += ("<center><table id=\"indexWords\"><thead><tr id=\"head\">");*/
		/*document.getElementById("resultBox").innerHTML += ("<th>Word</th><th>File Name</th><th>Line Nos</th></tr></thead><br>");*/
		for (var i = 0; i < indexes.length-1; i++) {
			wordTable += "<tr id=\"row\">";
			wordTable += "<td id=\"word\">" + origWords[indexes[i]] + "</td>";
			wordTable += "<td id=\"file-name\">" + origFiles[indexes[i]] + "</td>";
			wordTable += "<td id=\"line-nos\">" + origLineNo[indexes[i]] + "</td>";
			wordTable += "</tr>";
			/* document.getElementById("resultBox").innerHTML += ("<tr id=\"row\">");*/
			/* document.getElementById("resultBox").innerHTML += ("<td id=\"word\">" + origWords[indexes[i]] + "</td>");*/
			/* document.getElementById("resultBox").innerHTML += ("<td id=\"file-name\">" + origFiles[indexes[i]] + "</td>");*/
			/* document.getElementById("resultBox").innerHTML += ("<td id=\"file-name\">" + origFiles[indexes[i]] + "</td>");*/
			/* document.getElementById("resultBox").innerHTML += ("</tr><br>");*/
		}
		wordTable += "</table></center>";
		/*document.getElementById("resultBox").innerHTML += ("</table></center>");*/
	}
	/*if(sortedOrigWords.indexOf(word)!=-1) {
		var index = sortedOrigWords.indexOf(word);
		document.getElementById("resultBox").innerHTML += ("Word found at " + index);
	}
	else {
		document.getElementById("resultBox").innerHTML += ("Word not found");
	}*/
	var t1 = performance.now();
	document.getElementById("resultBox").innerHTML = (wordSearch + "Your query took " + (t1 - t0) + " milliseconds to execute.</center><br>");
	document.getElementById("resultBox").innerHTML += (wordTable);
}

/* getThreeColumnsOfTable - creates 3 arrays*/
function getThreeColumnsOfTable () {
	var tableID = document.getElementById("indexWords");
	var trTags = tableID.getElementsByTagName("tr");
	var numberOfRows = trTags.length;

	for(var i = 1; i < numberOfRows; ++i) {
		/* i = 0 for thead*/
		var elementOne = trTags[i].getElementsByTagName("td")[0];
		origWords.push(elementOne.innerHTML);
	}
	for(var i = 1; i < numberOfRows; ++i) {
		/* i = 0 for thead*/
		var elementTwo = trTags[i].getElementsByTagName("td")[1];
		origFiles.push(elementTwo.innerHTML);
	}
	for(var i = 1; i < numberOfRows; ++i) {
		/* i = 0 for thead*/
		var elementThree = trTags[i].getElementsByTagName("td")[2];
		origLineNo.push(elementThree.innerHTML);
	}
}

/* populatePre - populates String into text*/
function populatePre(url) {
	console.log(url);
	/*document.getElementById('resultBox').innerHTML = "code<br>";*/
	/*document.getElementById('resultBox').innerHTML = (url + "<br>");*/
	var xhr = new XMLHttpRequest();
	/*document.getElementById('resultBox').innerHTML += ("Make request<br>");*/
	xhr.onload = function () {
		var codeString = this.responseText;
		/*document.getElementById('resultBox').innerHTML = ("onload<br>");*/
		/*document.getElementById('resultBox').innerHTML += ("<textarea readonly>"+codeString+"</textarea>");*/
		completePrintPre(codeString, url);
	}
	xhr.open('GET', url);
	xhr.send();
}

/* completePrintPre - Print file in a table format*/
function completePrintPre ( codeString, fileUrl ) {
	/*document.getElementById('resultBox').innerHTML = ("completePrintPre<br>");*/
	fileTitle = fileUrl.split("/");
	document.getElementById('file-title').innerHTML = fileTitle[fileTitle.length-1];
	document.getElementById("content").innerHTML = "";
	var table = document.getElementById("codeTable");
	table.innerHTML = "";
	var res = codeString.split("\n");
	var len= res.length;
	for (var i = 0; i < len; i++) {
		var row = table.insertRow(-1);
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		cell1.setAttribute("id",(i+1).toString());
		cell1.setAttribute("style","padding-left: 10px; padding-right: 10px;");
		cell2.setAttribute("id","codetext");
		var extension = fileUrl.split('.').pop();
		if(extension.toLowerCase() != 'html')
		{
			var newstring = res[i].replace(" ", "&nbsp;");
			cell1.innerHTML = (i+1).toString();
			cell2.innerHTML = (res[i]);
		}
		else {
			var textLenRow = parseInt((res[i].length)/80);
			if( textLenRow == 0) {
				textLenRow = 1;
			}
			var newstring = res[i].replace(" ", "&nbsp;");
			cell1.innerHTML = (i+1).toString();
			var textareaString = ("<textarea cols=\"80\" rows=\"" + textLenRow + "\"readonly>" + newstring + "</textarea>");
			cell2.innerHTML = (textareaString);
		}
	}
	document.getElementById("content").innerHTML = "<br><br>";
}


/** Extra Content**/
/* Print someArray either or resultBox div or console log*/
function printArray (someArray) {
	var lengthOfArray = someArray.length;
	/*document.getElementById("resultBox").innerHTML += ("Print Function Called: " + lengthOfArray + "<br>");*/
	for(var i = 0; i < lengthOfArray; ++i) {
		/*document.getElementById("resultBox").innerHTML += (someArray[i] + "<br>");*/
		console.log(someArray[i]);
	}
}

/* Copy values in sourceArray to destArray*/
function copyArray (sourceArray, destArray) {
	var lengthOfArray = sourceArray.length;
	/*document.getElementById("resultBox").innerHTML += ("Copy Function Called: " + lengthOfArray + "<br>");*/
	for(var i = 0; i < lengthOfArray; ++i) {
		destArray[i] = sourceArray[i];
	}
}

/* Optimized Version*/
function getAllIndexesOptimized(arr, val) {
	var indexes = [];
	var index = -1, nextIndex = -1, flag = 0;
	var startLetter = val.charAt(0);
	console.log(startLetter);
	if ( startLetter in mapLetterPosition ) {
		index = mapLetterPosition[startLetter];
		console.log(index);
		for (var key in mapLetterPosition) {
			if ( flag ) {
				nextIndex = mapLetterPosition[key];
				break;
			}
			if( mapLetterPosition[key]==index ) {
				flag = 1;
			}
		}
		console.log(nextIndex);
		indexes = binarySearch(origWords, val, index, nextIndex+1);
	}
	else {
		indexes.push(index);
	}
	return indexes;
}

function binarySearch(arr, val, left, right) {
	var indexes = [], flag = 0;
	console.log("binarySearch");
	console.log(left);
	console.log(right);
	console.log((left+right)/2);
	while (left <= right ) {
		var middle = (left+right)/2;
		middle = Math.round(middle); 
		/*console.log(middle);*/
		/*console.log(origWords[middle]);*/
		if( origWords[middle]==val ) {
			flag = 1;
			indexes.push(middle);
			break;
		}
		if( origWords[middle] < val ) {
			left = middle + 1;
		}
		else {
			right = middle - 1;
		}
	}
	if ( !flag ) {
		indexes.push(-1);
	}
	else {
		console.log("mapLetterFrequency");
		console.log(mapLetterFrequency[val]);
		console.log("position");
		for (var i = middle+1; i < middle+mapLetterFrequency[val]; i++) {
			console.log(i);
			indexes.push(i);
		}
	}
	return indexes;
}

/* Search for word typed in search box and make the necessary table output*/
function searchWordOptimized (word) {
	document.getElementById("content").innerHTML = "";
	document.getElementById("resultBox").innerHTML = "";
	/*var dummyArray = new Array();*/
	/*copyArray(workWords, dummyArray);*/
	/*dummyArray.sort()*/
	var t0 = performance.now();
	var wordSearch = "<center>You've queried for " + word + ". ";
	var wordNotFound = "<center>Word <b>"+word+"</b> not found</center><br>";
	var indexes = getAllIndexesOptimized(origWords, word);
	console.log("newIndexes");
	printArray(indexes);
	/*document.getElementById("resultBox").innerHTML += (indexes.length + "<br>");*/
	/*document.getElementById("resultBox").innerHTML += (indexes[indexes.length-1] + "<br>");*/
	if ( indexes.length == 1 && indexes[0] == -1 ) {
		document.getElementById("resultBox").innerHTML += (wordNotFound);
		return -1;
	}
	else {
		var wordTable = "<center><table id=\"indexWords\"><thead><tr id=\"head\">";
		wordTable += "<th>Word</th><th>File Name</th><th>Line Nos</th></tr></thead>";
		/*document.getElementById("resultBox").innerHTML += ("<center><table id=\"indexWords\"><thead><tr id=\"head\">");*/
		/*document.getElementById("resultBox").innerHTML += ("<th>Word</th><th>File Name</th><th>Line Nos</th></tr></thead><br>");*/
		for (var i = 0; i < indexes.length-1; i++) {
			wordTable += "<tr id=\"row\">";
			wordTable += "<td id=\"word\">" + origWords[indexes[i]] + "</td>";
			wordTable += "<td id=\"file-name\">" + origFiles[indexes[i]] + "</td>";
			wordTable += "<td id=\"line-nos\">" + origLineNo[indexes[i]] + "</td>";
			wordTable += "</tr>";
			/* document.getElementById("resultBox").innerHTML += ("<tr id=\"row\">");*/
			/* document.getElementById("resultBox").innerHTML += ("<td id=\"word\">" + origWords[indexes[i]] + "</td>");*/
			/* document.getElementById("resultBox").innerHTML += ("<td id=\"file-name\">" + origFiles[indexes[i]] + "</td>");*/
			/* document.getElementById("resultBox").innerHTML += ("<td id=\"file-name\">" + origFiles[indexes[i]] + "</td>");*/
			/* document.getElementById("resultBox").innerHTML += ("</tr><br>");*/
		}
		wordTable += "</table></center>";
		/*document.getElementById("resultBox").innerHTML += ("</table></center>");*/
	}
	/*if(sortedOrigWords.indexOf(word)!=-1) {
		var index = sortedOrigWords.indexOf(word);
		document.getElementById("resultBox").innerHTML += ("Word found at " + index);
	}
	else {
		document.getElementById("resultBox").innerHTML += ("Word not found");
	}*/
	var t1 = performance.now();
	document.getElementById("resultBox").innerHTML = (wordSearch + "Your query took " + (t1 - t0) + " milliseconds to execute.</center><br>");
	document.getElementById("resultBox").innerHTML += (wordTable);
}

function createMapLetterPosition(someArray) {
	var numberOfRows = someArray.length;
	for(var i = 0; i < numberOfRows; ++i) {
		var startLetter = someArray[i].charAt(0);
		if ( !(startLetter in mapLetterPosition) ) {
			mapLetterPosition[startLetter] = i;
		}
	}
}

function createMapLetterFrequency(someArray) {
	var numberOfRows = someArray.length;
	for(var i = 0; i < numberOfRows; ++i) {
		if ( !(origWords[i] in mapLetterFrequency) ) {
			mapLetterFrequency[origWords[i]] = 1;
		}
		else {
			mapLetterFrequency[origWords[i]] += 1;
		}
	}
}

function printMap( someMap ) {
	for (var key in someMap) {
		console.log(someMap[key]);
	}
}


