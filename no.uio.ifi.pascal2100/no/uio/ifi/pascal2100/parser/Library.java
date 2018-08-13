package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.CodeFile;

public class Library extends Block {
	
	
	/*EnumType false;
	EnumType true;*/
	
		PascalDecl constdecl=new ConstDecl("eol",lineNum);
	 PascalDecl procdel=new ProcDecl("write", lineNum);
	 PascalDecl typedeclint=new TypeDecl("Integer", lineNum);
	 PascalDecl typedeclchar=new TypeDecl("char", lineNum);
	 PascalDecl typedeclboolean=new TypeDecl("boolean", lineNum);
	 PascalDecl enumliteralt = new EnumLiteral("true",lineNum);
	 PascalDecl enumliteralf = new EnumLiteral("false",lineNum);
	
	 

	public Library(int n) {super(n);
	
	
	 /*PascalDecl constdecl=new ConstDecl("eol", linenum);
	 PascalDecl procdel=new ProcDecl("write", linenum);
	 PascalDecl typedeclint=new TypeDecl("Integer", linenum);
	 PascalDecl typedeclchar=new TypeDecl("char", linenum);
	 PascalDecl typedeclboolean=new TypeDecl("boolean", linenum);
	 PascalDecl enumliteralt = new EnumLiteral("true",linenum);
	 PascalDecl enumliteralf = new EnumLiteral("false",linenum);
	addDecl(constdecl.name, constdecl);
	addDecl(typedeclint.name, typedeclint);
	addDecl(procdel.name,procdel);
	addDecl(typedeclchar.name,typedeclchar);
	addDecl(typedeclboolean.name,typedeclboolean);*/
	
	
	
	}
	

	public Library() {
		
		this.addDecl(constdecl.name, constdecl);
		this.addDecl(typedeclint.name, typedeclint);
		this.addDecl(procdel.name,procdel);
		this.addDecl(typedeclchar.name,typedeclchar);
		this.addDecl(typedeclboolean.name,typedeclboolean);
		
	}



	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "< lib> " + " in the lib";
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub

	}



	public void genCode(CodeFile code) {
		// TODO Auto-generated method stub
		
	}

}
