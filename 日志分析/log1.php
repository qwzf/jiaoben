<?php
/**
使用方法：在其他php文件中 include('log.php');
需要新建'log.txt'，文件，并在当前目录 chmod 777 *
**/
error_reporting(0);
date_default_timezone_set('Asia/Shanghai');
$ip = $_SERVER['REMOTE_ADDR']; //记录访问者的ip
$filename = $_SERVER['PHP_SELF'];   //访问者要访问的文件名
$parameter = $_SERVER['QUERY_STRING']; //访问者要请求的参数
$time = date('Y-m-d H:i:s',time()); //访问时间
$method = $_SERVER['REQUEST_METHOD']; //请求方式
$post= isset($GLOBALS['HTTP_RAW_POST_DATA']) ? $GLOBALS['HTTP_RAW_POST_DATA'] : file_get_contents("php://input");
$logadd = '来访时间：'.$time.'-->访客ip：'.$ip.'-->访问路径：/'.$filename.'?'.$parameter.'-->请求方式：'.$method."post的数据为:".$post."\r\n";

$file = '/var/www/html/log.txt';//存放日志的地方
file_put_contents($file, $logadd, FILE_APPEND | LOCK_EX);
?>