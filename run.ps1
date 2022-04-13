function Worker{
    $pythonw = Get-ChildItem -Recurse *pythonw.exe | % {$_.FullName}
    $file_run = Get-ChildItem -Recurse *run.py | % {$_.FullName}
    try{
        Start-Process $pythonw $file_run
    }catch{
        Write-Host "Pythonw -> $pythonw, File_run -> $file_run. Start error."
    }
}

$void = Worker