package no.uio.ifi.pascal2100.parser;

import java.util.*;
import java.util.List;

import no.uio.ifi.pascal2100.scanner.*;
import no.uio.ifi.pascal2100.main.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind .* ;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>Block</h1>
 *
 * <p>Parse a Pascal block as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class Block extends PascalSyntax {
			 
	public Program context;
	ConstDeclPart cdp;
	TypeDeclPart tdp;
	VarDeclPart vdp;
	public static List <ProcDecl>procdecllist = new ArrayList<ProcDecl>(); 
	public static List <FuncDecl>funcdecllist = new ArrayList<FuncDecl>(); 
	ProcDecl pd;
	FuncDecl fd;
	StatmList st;
	HashMap<String,PascalDecl> decls = new HashMap<String,PascalDecl>();

	
	Block outerScope;

	public FuncDecl firstfuncdecl = null;
	public ProcDecl firstprocdecl = null;
	public ProcDecl prcDc;
	
	public Block(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	public Block(){
		
	}

	
		@Override public String identify() {
			return "<block> " + " on line " + lineNum;
			}
		
	public void addDecl(String id, PascalDecl d) {
		if (decls.containsKey(id))
		d.error(id + " declared twice in same block!");
		decls.put(id, d);
		/*System.out.println(decls.keySet());*/
		}
	
	
		@Override
		public void check(Block curScope, Library lib) {
			
			outerScope= lib;
			
			/*System.out.println("liberay keys "+lib.decls.keySet());*/
		if ( cdp!= null) {
			System.out.println("cdp is not null");
			cdp.check(this, lib);
		for (ConstDecl cd: cdp.constants) {
			System.out.println("add decl called "+cd.name);
			addDecl(cd.name, cd);
		
		}
		}
		if (tdp!= null) {
			tdp.check(this, lib);
		for (TypeDecl tdc: tdp.typer) {
			System.out.println("block tdc name"+ tdc.name);
			addDecl(tdc.name, tdc);
		
		
		}
		}
		if (vdp!= null) {
			vdp.check(this, lib);
		for (VarDecl vdc: vdp.vardeclat) {
			System.out.println("block vdc name"+ vdc.name);
		addDecl(vdc.name, vdc);
		
		}
		}
		while(firstfuncdecl != null || firstprocdecl != null ){
		FuncDecl funcdel=firstfuncdecl;
		if(funcdel != null){
			funcdel.check(this, lib);
			for (FuncDecl fdc : funcdel.funcdecllist){
				System.out.println("func decl name"+fdc.name);
				addDecl(fdc.name,fdc);
			}
			funcdel=funcdel.nextfunc;
		}
		
		ProcDecl procdel= firstprocdecl	;
		if(procdel!=null){
			System.out.println("procdecl blockis not null");
			procdel.check(this, lib);
			for (ProcDecl pdc : procdel.procdecllist){
				System.out.println("proc decl name"+pdc.name);
				addDecl(pdc.name,pdc);
			}
			procdel=procdel.nextproc;
		}
		}
		
		if (st != null) st.check(curScope, lib);
		System.out.println("keys"+decls.keySet());
	}
		
		PascalDecl findDecl(String id, PascalSyntax where) {
			
			PascalDecl d = decls.get(id);
			if (d != null) {
				System.out.println("innerscope block1"+id+where+"  "+lineNum);
			Main.log.noteBinding(id, where, d);
			return d;
			}
			if (outerScope != null){
				System.out.println("outerscope block"+id+where+"  "+lineNum);
			return outerScope.findDecl(id,where);
			}
			where.error("Name " + id + " is unknown!");
			return null; // Required by the Java compiler.
			}

	
    /**
     * Parse a block.
     * @param Scanner Tokens.
     * @return the Block object of the parse tree.
     */

	public static Block parse(Scanner s) {
		
	
		// TODO Auto-generated method stub
		 FuncDecl tempfunc = null;
		 ProcDecl tempproc = null;
		enterParser("block");
		/*System.out.println("entering perser block");*/
	
		Block block = new Block(s.curLineNum());
		/*System.out.println( "vdp"+ s.curToken.kind);*/
		
		// Parse the constant Token if any
		if(s.curToken.kind==constToken) {	
			block.cdp = ConstDeclPart.parse(s);block.cdp.b=block;
		}
		// Parse the type Token if any
		if(s.curToken.kind==typeToken){
			block.tdp = TypeDeclPart.parse(s); block.tdp.b=block;
		}
		//Parse the variable Token if any
		if(s.curToken.kind==varToken){
			block.vdp = VarDeclPart.parse(s); block.vdp.b=block;	
		}
		
		
		// parse the function token or procedure token
		
		
		if (s.curToken.kind != beginToken)
		{
			
			while(s.curToken.kind ==  functionToken || s.curToken.kind ==procedureToken){
				
			
		switch(s.curToken.kind ){
			case functionToken:
				FuncDecl localfunc= FuncDecl.parse(s);
				
				if (tempfunc == null){
					block.firstfuncdecl=tempfunc=localfunc;
				}
				else{
					tempfunc.nextfunc=tempfunc=localfunc;
					tempfunc=localfunc;
				}
				
				break;
			case procedureToken:
				ProcDecl localproc= ProcDecl.parse(s);
				
				if (tempproc == null){
					block.firstprocdecl=tempproc=localproc;
				}
				else{
					tempproc.nextproc=tempproc=localproc;
					tempproc=localproc;
				}
				
				break;
				default: break;
		}
			}
		}
	
	
		s.skip(beginToken);
		block.st=StatmList.parse(s);block.st.b=block;
		
		
		s.skip(endToken);
	
		leaveParser("block");
		
		
		return block;
		
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		if(cdp!= null) cdp.prettyPrint();
		if(tdp!= null) tdp.prettyPrint();
		if(vdp!= null) vdp.prettyPrint();
		

		
		FuncDecl funcList= firstfuncdecl;
		 while (funcList != null) {
			 funcList.prettyPrint();
			 funcList = funcList.nextfunc;
	          
	    }
		 ProcDecl ProcList= firstprocdecl;
		 while (ProcList != null) {
			 ProcList.prettyPrint();
			 ProcList = ProcList.nextproc;
	          
	    }
		
		Main.log.prettyPrintLn();
		Main.log.prettyPrintLn();
		Main.log.prettyOutdent();
		
		Main.log.prettyPrintLn("begin ");
		Main.log.prettyIndent();
		if (st!=null)st.prettyPrint();
		Main.log.prettyOutdent();
		Main.log.prettyPrint("end");
		
	}


}
