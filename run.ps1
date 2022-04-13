function Worker{
    $file_run = Get-ChildItem -Recurse *run.py | % {$_.FullName}
    if ($file_run){
        $result = python --version
        if ($result){
            Start-Process pythonw $file_run
        }
    }
}

$void = Worker