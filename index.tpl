<html>
<head>
	<title>Verk2</title>
	<link rel="stylesheet" type="text/css" href="static/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="static/my.css">
	<script type="text/javascript" src="static/jquery.js"></script>
	<script type="text/javascript" src="static/bootstrap.min.js"></script>
</head>
<body>
	<div class="container">

		<!-- Top -->
		<div class="row">
			<div class="col-md-6 col-xs-6">
				<ul class="list-inline">

					%if defined('statusrows'):
				    <li>New:         <strong> {{ statusrows[0] }} </strong></li>
				    <li>In progress: <strong> {{ statusrows[1] }} </strong></li>
				    <li>Waiting:     <strong> {{ statusrows[2] }} </strong></li>
				    <li>Ready:       <strong> {{ statusrows[3] }} </strong></li>

					%else:
						<p>Only works in Overview still</p>
					%end


				</ul>
			</div>
			<div class="col-md-5 col-xs-5">
				<div class="input-group">
				  <span class="input-group-addon">?</span>
				  <input type="text" class="form-control" placeholder="Search">
				</div>
			</div>
			<div class="col-md-1 col-xs-1">
				<a href="">Log Out</a>
			</div>
		</div> <!-- end row Top -->

		<hr>

		<!-- Menu -->
		<div class="row">
			<div class="btn-group btn-group-justified btn-group-lg">
				<a href="create" class="btn btn-default">Create</a>
				<a href="overview" class="btn btn-default">Overview</a>
				<a href="clients" class="btn btn-default">Clients</a>
				<a href="users" class="btn btn-default">Users</a>
				<a href="settings" class="btn btn-danger" >Settings</a>
			</div>
		</div> <!-- End row menu -->


		<!--  Should we INJECT stuff here using the base ? -->

	<!-- Rest is in footer.tpl -->