<h1>Setting Up Golang Environment on Mac OS</h1>

<div>
<h2>Installing Golang</h2>
<ol>
<li>Download Golang from <a href="https://golang.org/dl/">GolangDownload</a> and extract it using the following command:<br>
 <b><i>$ sudo tar -C /usr/local -xzf "downloadedfilename"</i></b> .</li>
<li>Alternatively, you can use <i><b>brew install go</i></b> to get it.</li>
<li>Next, you need to set the export path, To do this, open up your .bash_profile or .bashrc file.</li>

<b><i>export PATH=$PATH:/usr/local/go/bin <br>
export GOPATH=$HOME/go. <i></b>
</ol>
</div>

<div>
<h2>Setting Up Sublime</h2>
<ol>
<li>Install <a href="https://packagecontrol.io/installation">Package Control System</a> if you haven't already. </li>
<li>Now you need to install GoSublime using PCS.</li>
<li>Press <b>CMD+Shift+P</b> and then  "Package control: Install Package"</li>
<li>Search for Go and install it.</li>
<li>Then, go to <i>Preferences -> Package Settings -> GoLang Config -> Settings - User</i> and add the following line.
<br>
<b><i>
{ <br>
    "env": { <br>
        "GOPATH": "$HOME/go", <br>
        "GOROOT": "/usr/local/go" <br>
    }<br>
}
</i></b>
</li>
<li>Save and restart.</li>
</ol>
</div>
<h2>Setting up Golang in  Visual Studio Code </h2>
<div>
<ol>
<li>Open VS code. </li>
<li>Go to extensions.</li>
<li>Search for Go and install the first package.</li>
<li>Reload Go and restart VS code.</li>
<li>Create a sample hello world code and save it. (The VS code will ask you to install the missing plugins. Install them and run your program)</li>
</ol>
</div>
<h2>Running Go programs:</h2>
Use the following Commands to run/compile the .go file
<ul>
<li>go run filename.go</li>
<li>go build filename.go</li>
<li>go install filename.go</li>
</ul>


<br><br>
<h3>Thanks ! </h3>
